from typing import List

from fastapi import Depends, HTTPException

from app.jwt_utils import get_current_user
from app.models import UserModel


# class RoleChecker:
#     def __init__(self, allowed_roles: List):
#         self.allowed_roles = allowed_roles

#     def __call__(self, current_user: UserModel = Depends(get_current_user)):
#         if current_user.roles not in self.allowed_roles:
#             print(f"User with role {current_user.roles} not in {self.allowed_roles}")
#             raise HTTPException(status_code=403, detail="Operation not permitted")


class RoleChecker:
    def __init__(self, role_name: str):
        self.role_name = role_name

    def __call__(self, current_user: UserModel = Depends(get_current_user)):
        if current_user.roles not in self.allowed_roles:
            print(f"User with role {current_user.roles} not in {self.allowed_roles}")
            raise HTTPException(status_code=403, detail="Operation not permitted")
