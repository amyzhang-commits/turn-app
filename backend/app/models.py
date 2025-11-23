from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    game_sessions = relationship("GameSession", back_populates="user")

class GameSession(Base):
    __tablename__ = "game_session"

    session_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    session_name = Column(Text, nullable=True)
    start_time = Column(DateTime(timezone=True), server_default=func.now())
    end_time = Column(DateTime(timezone=True), nullable=True)
    status = Column(Text, nullable=False, default="active")  # active, paused, ended
    user_score = Column(Integer, default=0)
    llm_score = Column(Integer, default=0)
    reward_assigned = Column(Text, nullable=True)

    # Relationships
    user = relationship("User", back_populates="game_sessions")
    logs = relationship("GameSessionLog", back_populates="session")
    tracked_actions = relationship("TrackedAction", back_populates="session")

class ActionLibrary(Base):
    __tablename__ = "action_library"

    library_id = Column(Integer, primary_key=True, index=True)
    created_from_session_id = Column(Integer, ForeignKey("game_session.session_id"), nullable=True)
    action_description = Column(Text, nullable=False)
    default_user_movement = Column(Integer, nullable=False)
    default_llm_movement = Column(Integer, nullable=False)
    times_used = Column(Integer, default=0)
    user_created = Column(Boolean, default=False)

    # Relationships
    session = relationship("GameSession", foreign_keys=[created_from_session_id])
    tracked_actions = relationship("TrackedAction", back_populates="library_action")

class TrackedAction(Base):
    __tablename__ = "tracked_actions"

    action_id = Column(Integer, primary_key=True, index=True)
    library_id = Column(Integer, ForeignKey("action_library.library_id"), nullable=True)
    session_id = Column(Integer, ForeignKey("game_session.session_id"), nullable=False)
    action_description = Column(Text, nullable=True)  # NULL when library_id is set
    user_movement = Column(Integer, nullable=False)
    llm_movement = Column(Integer, nullable=False)

    # Relationships
    session = relationship("GameSession", back_populates="tracked_actions")
    library_action = relationship("ActionLibrary", back_populates="tracked_actions")
    logs = relationship("GameSessionLog", back_populates="action")

class GameSessionLog(Base):
    __tablename__ = "game_session_logs"

    log_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("game_session.session_id"), nullable=False)
    action_id = Column(Integer, ForeignKey("tracked_actions.action_id"), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    optional_note = Column(Text, nullable=True)

    # Relationships
    session = relationship("GameSession", back_populates="logs")
    action = relationship("TrackedAction", back_populates="logs")
