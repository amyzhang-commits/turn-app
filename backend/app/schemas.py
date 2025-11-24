from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# User schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    user_id: int
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None

# Game Session schemas
class GameSessionCreate(BaseModel):
    session_name: Optional[str] = None
    selected_action_ids: list[int] = []

class GameSessionUpdate(BaseModel):
    session_name: Optional[str] = None
    status: Optional[str] = None
    end_time: Optional[datetime] = None

class GameSessionResponse(BaseModel):
    session_id: int
    user_id: int
    session_name: Optional[str]
    start_time: datetime
    end_time: Optional[datetime]
    status: str
    user_score: int
    llm_score: int
    reward_assigned: Optional[str]

    class Config:
        from_attributes = True

# Action Library schemas
class ActionLibraryCreate(BaseModel):
    action_description: str
    default_user_movement: int
    default_llm_movement: int
    created_from_session_id: Optional[int] = None

class ActionLibraryResponse(BaseModel):
    library_id: int
    action_description: str
    default_user_movement: int
    default_llm_movement: int
    times_used: int
    user_created: bool

    class Config:
        from_attributes = True

# Tracked Action schemas
class TrackedActionCreate(BaseModel):
    session_id: int
    library_id: Optional[int] = None
    action_description: Optional[str] = None
    user_movement: int
    llm_movement: int

class TrackedActionResponse(BaseModel):
    action_id: int
    session_id: int
    library_id: Optional[int]
    action_description: Optional[str]
    user_movement: int
    llm_movement: int

    class Config:
        from_attributes = True

# Game Session Log schemas
class GameSessionLogCreate(BaseModel):
    session_id: int
    action_id: int
    optional_note: Optional[str] = None

class GameSessionLogResponse(BaseModel):
    log_id: int
    session_id: int
    action_id: int
    timestamp: datetime
    optional_note: Optional[str]

    class Config:
        from_attributes = True
