from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int]
    roles: list = []


class UserBase(BaseModel):
    full_name: str
    username: str
    is_active: Optional[bool] = True


class RoleBase(BaseModel):
    role_name: str


class CreateAndUpdateRole(RoleBase):
    ...


class CreateAndUpdateUser(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    roles: list = []

    class Config:
        orm_mode = True


class RoleResponse(RoleBase):
    id: int
    users: list = []

    class Config:
        orm_mode = True
