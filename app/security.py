from typing import List

from fastapi import Depends, HTTPException

from app.jwt_utils import get_current_user
from app.models import UserModel
from app.schemas import RoleBase, UserResponse


class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: UserModel = Depends(get_current_user)):
        if current_user.roles not in self.allowed_roles:
            print(f"User with role {current_user.roles} not in {self.allowed_roles}")
            raise HTTPException(status_code=403, detail="Operation not permitted")


class AuthorityChecker:
    def __init__(self, role_name: str):
        self.role_name = role_name

    def __call__(self, current_user: UserModel = Depends(get_current_user)):
        print("AuthorityChecker")
        print(f"self.role_name: {self.role_name}")
        user_roles = [role.role_name for role in current_user.roles]
        print(f"Current User Roles: {user_roles}")
        if self.role_name not in user_roles:
            msg = f"User with role {self.role_name} not in {user_roles}"
            raise HTTPException(
                status_code=403, detail={"msg": "Operation not permitted", "desc": msg}
            )
        return UserResponse(
            id=current_user.id,
            full_name=current_user.full_name,
            username=current_user.username,
            is_active=current_user.is_active,
            roles=current_user.roles,
        )
