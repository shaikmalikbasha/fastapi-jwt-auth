from fastapi import APIRouter, Depends

from app.constants import ADMIN_ALLOWED_ROLES, MANAGER_ALLOWED_ROLES, USER_ALLOWED_ROLES
from app.security import AuthorityChecker, RoleChecker

admin_allowed_roles = RoleChecker(ADMIN_ALLOWED_ROLES)
manager_allowed_roles = RoleChecker(MANAGER_ALLOWED_ROLES)
user_allowed_roles = RoleChecker(USER_ALLOWED_ROLES)


admin_required = AuthorityChecker("ADMIN")
manager_required = AuthorityChecker("MANAGER")
user_required = AuthorityChecker("USER")

admin_router = APIRouter(prefix="/admin", tags=["Admin Routes"])
manager_router = APIRouter(prefix="/manager", tags=["Admin Routes"])
user_router = APIRouter(prefix="/admin", tags=["Admin Routes"])


# @admin_router.get("/", dependencies=[Depends(admin_allowed_roles)])
# async def admin_home():
#     return {"msg": "Admin Route", "desc": "He has authority to access this resource"}


@admin_router.get("/")
async def admin_home(current_user=Depends(admin_required)):
    return {
        "msg": "Admin Route",
        "desc": "He(Admin) has authority to access this resource",
        "logged_user": current_user,
    }


@manager_router.get("/")
async def manager_home(current_user=Depends(manager_required)):
    return {
        "msg": "Manager Route",
        "desc": "He(Manager) has authority to access this resource",
        "logged_user": current_user,
    }


@user_router.get("/")
async def user_home(current_user=Depends(user_required)):
    return {
        "msg": "User Route",
        "desc": "He(User) has authority to access this resource",
        "logged_user": current_user,
    }
