from pydantic import BaseModel
from typing import List, Optional, Dict


class TestCard(BaseModel):
    id: int
    slug: str
    title: str
    shortTitle: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    icon: Optional[str] = None
    buttonText: Optional[str] = None
    order: int

    class Config:
        from_attributes = True


class OptionOut(BaseModel):
    id: int
    text: str
    optionKey: Optional[str] = None

    class Config:
        from_attributes = True


class QuestionOut(BaseModel):
    id: int
    text: str
    order: int
    options: List[OptionOut]

    class Config:
        from_attributes = True


class TestDetail(BaseModel):
    id: int
    slug: str
    title: str
    description: Optional[str] = None
    icon: Optional[str] = None
    category: Optional[str] = None
    questions: List[QuestionOut]

    class Config:
        from_attributes = True


class SubmitTestRequest(BaseModel):
    option_ids: List[int]


class SubmitTestResponse(BaseModel):
    resultTitle: str
    resultDescription: str
    scores: Dict[str, float]

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class AuthUser(BaseModel):
    id: int
    username: str
    email: str


class AuthResponse(BaseModel):
    message: str
    user: AuthUser