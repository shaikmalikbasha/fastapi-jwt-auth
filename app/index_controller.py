from fastapi import APIRouter, Depends

from app.constants import ADMIN_ALLOWED_ROLES, MANAGER_ALLOWED_ROLES, USER_ALLOWED_ROLES
from app.security import RoleChecker

# admin_allowed_roles = RoleChecker(ADMIN_ALLOWED_ROLES)
# manager_allowed_roles = RoleChecker(MANAGER_ALLOWED_ROLES)
# user_allowed_roles = RoleChecker(USER_ALLOWED_ROLES)


admin_allowed_roles = RoleChecker("ADMIN")
manager_allowed_roles = RoleChecker("MANAGER")
user_allowed_roles = RoleChecker("USER")

admin_router = APIRouter(prefix="/admin", tags=["Admin Routes"])


@admin_router.get("/", dependencies=[Depends(admin_allowed_roles)])
async def admin_home():
    return {"msg": "Admin Route", "desc": "He has authority to access this resource"}


manager_router = APIRouter(prefix="/manager", tags=["Admin Routes"])


@manager_router.get("/", dependencies=[Depends(manager_allowed_roles)])
async def manager_home():
    return {
        "msg": "Admin Route",
        "desc": "He(Manager) has authority to access this resource",
    }


user_router = APIRouter(prefix="/admin", tags=["Admin Routes"])


@user_router.get("/", dependencies=[Depends(user_allowed_roles)])
async def user_home():
    return {
        "msg": "User Route",
        "desc": "He(User) has authority to access this resource",
    }
