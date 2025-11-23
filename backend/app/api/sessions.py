from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.database import get_db
from app.models import User, GameSession
from app.schemas import GameSessionCreate, GameSessionUpdate, GameSessionResponse
from app.auth import get_current_user

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
    db.commit()
    db.refresh(new_session)
    return new_session

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
