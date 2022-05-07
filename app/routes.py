from fastapi import APIRouter

from app import auth, index_controller, role_controller, user_controller

router = APIRouter()

router.include_router(user_controller.router)
router.include_router(role_controller.router)
router.include_router(auth.auth_router)
router.include_router(index_controller.admin_router)
router.include_router(index_controller.manager_router)
router.include_router(index_controller.user_router)
