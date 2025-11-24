from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.database import get_db
from app.models import User, GameSession, SelectedAction, TrackedAction, ActionLibrary
from app.schemas import GameSessionCreate, GameSessionUpdate, GameSessionResponse
from app.auth import get_current_user
import io
import csv

router = APIRouter()

@router.post("/", response_model=GameSessionResponse, status_code=status.HTTP_201_CREATED)
def create_session(
    session_data: GameSessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_session = GameSession(
        user_id=current_user.user_id,
        session_name=session_data.session_name,
        status="active"
    )
    db.add(new_session)
    db.flush()  # Get session_id before committing

    # Add selected actions
    for action_id in session_data.selected_action_ids:
        selected_action = SelectedAction(
            session_id=new_session.session_id,
            library_id=action_id
        )
        db.add(selected_action)

    db.commit()
    db.refresh(new_session)
    return new_session

@router.get("/{session_id}/selected-actions")
def get_session_selected_actions(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Verify session belongs to user
    session = db.query(GameSession).filter(
        GameSession.session_id == session_id,
        GameSession.user_id == current_user.user_id
    ).first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )

    selected = db.query(SelectedAction).filter(
        SelectedAction.session_id == session_id
    ).all()

    return [s.library_id for s in selected]

@router.get("/", response_model=List[GameSessionResponse])
def get_user_sessions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    status: str = None
):
    query = db.query(GameSession).filter(GameSession.user_id == current_user.user_id)
    if status:
        query = query.filter(GameSession.status == status)
    sessions = query.order_by(GameSession.start_time.desc()).all()
    return sessions

@router.get("/{session_id}", response_model=GameSessionResponse)
def get_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    session = db.query(GameSession).filter(
        GameSession.session_id == session_id,
        GameSession.user_id == current_user.user_id
    ).first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )

    return session

@router.patch("/{session_id}", response_model=GameSessionResponse)
def update_session(
    session_id: int,
    session_update: GameSessionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    session = db.query(GameSession).filter(
        GameSession.session_id == session_id,
        GameSession.user_id == current_user.user_id
    ).first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )

    # Update fields
    if session_update.session_name is not None:
        session.session_name = session_update.session_name
    if session_update.status is not None:
        session.status = session_update.status
        if session_update.status == "ended" and session.end_time is None:
            session.end_time = datetime.utcnow()
    if session_update.end_time is not None:
        session.end_time = session_update.end_time

    db.commit()
    db.refresh(session)
    return session

@router.post("/{session_id}/pause", response_model=GameSessionResponse)
def pause_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    session = db.query(GameSession).filter(
        GameSession.session_id == session_id,
        GameSession.user_id == current_user.user_id
    ).first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )

    session.status = "paused"
    db.commit()
    db.refresh(session)
    return session

@router.post("/{session_id}/resume", response_model=GameSessionResponse)
def resume_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    session = db.query(GameSession).filter(
        GameSession.session_id == session_id,
        GameSession.user_id == current_user.user_id
    ).first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )

    session.status = "active"
    db.commit()
    db.refresh(session)
    return session

@router.post("/{session_id}/end", response_model=GameSessionResponse)
def end_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    session = db.query(GameSession).filter(
        GameSession.session_id == session_id,
        GameSession.user_id == current_user.user_id
    ).first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )

    session.status = "ended"
    session.end_time = datetime.utcnow()
    db.commit()
    db.refresh(session)
    return session

@router.get("/{session_id}/export")
def export_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Verify session belongs to user
    session = db.query(GameSession).filter(
        GameSession.session_id == session_id,
        GameSession.user_id == current_user.user_id
    ).first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )

    # Get all tracked actions for this session
    tracked_actions = db.query(TrackedAction).filter(
        TrackedAction.session_id == session_id
    ).all()

    # Create CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)

    # Write session info header
    writer.writerow(['Session Information'])
    writer.writerow(['Session ID', session.session_id])
    writer.writerow(['Session Name', session.session_name or 'Unnamed'])
    writer.writerow(['Start Time', session.start_time])
    writer.writerow(['End Time', session.end_time or 'Ongoing'])
    writer.writerow(['Status', session.status])
    writer.writerow(['Final User Score', session.user_score])
    writer.writerow(['Final LLM Score', session.llm_score])
    writer.writerow([])

    # Write actions data
    writer.writerow(['Actions Tracked'])
    writer.writerow(['Action ID', 'Description', 'User Points', 'LLM Points', 'Source'])

    for action in tracked_actions:
        # Get description from library if available
        if action.library_id:
            library_action = db.query(ActionLibrary).filter(
                ActionLibrary.library_id == action.library_id
            ).first()
            description = library_action.action_description if library_action else 'Unknown'
            source = 'Library'
        else:
            description = action.action_description or 'Custom'
            source = 'Custom (Session)'

        writer.writerow([
            action.action_id,
            description,
            action.user_movement,
            action.llm_movement,
            source
        ])

    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=session_{session_id}_export.csv"
        }
    )

@router.get("/export-all")
def export_all_sessions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Get all sessions for user
    sessions = db.query(GameSession).filter(
        GameSession.user_id == current_user.user_id
    ).order_by(GameSession.start_time.desc()).all()

    # Create CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)

    # Write sessions summary
    writer.writerow(['All Sessions Summary'])
    writer.writerow(['Session ID', 'Session Name', 'Start Time', 'End Time', 'Status', 'User Score', 'LLM Score', 'Duration (minutes)', 'Total Actions'])

    for session in sessions:
        # Calculate duration
        duration = ''
        if session.end_time and session.start_time:
            delta = session.end_time - session.start_time
            duration = round(delta.total_seconds() / 60, 1)

        # Count actions
        action_count = db.query(TrackedAction).filter(
            TrackedAction.session_id == session.session_id
        ).count()

        writer.writerow([
            session.session_id,
            session.session_name or 'Unnamed',
            session.start_time,
            session.end_time or 'Ongoing',
            session.status,
            session.user_score,
            session.llm_score,
            duration,
            action_count
        ])

    writer.writerow([])
    writer.writerow([])

    # Write detailed actions for each session
    writer.writerow(['Detailed Action Log'])
    writer.writerow(['Session ID', 'Session Name', 'Action ID', 'Description', 'User Points', 'LLM Points', 'Source'])

    for session in sessions:
        tracked_actions = db.query(TrackedAction).filter(
            TrackedAction.session_id == session.session_id
        ).all()

        for action in tracked_actions:
            if action.library_id:
                library_action = db.query(ActionLibrary).filter(
                    ActionLibrary.library_id == action.library_id
                ).first()
                description = library_action.action_description if library_action else 'Unknown'
                source = 'Library'
            else:
                description = action.action_description or 'Custom'
                source = 'Custom'

            writer.writerow([
                session.session_id,
                session.session_name or 'Unnamed',
                action.action_id,
                description,
                action.user_movement,
                action.llm_movement,
                source
            ])

    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=spade_app_all_data_export.csv"
        }
    )
