from fastapi import APIRouter
from app import user_controller, role_controller, auth


router = APIRouter()

router.include_router(user_controller.router)
router.include_router(role_controller.router)
router.include_router(auth.auth_router)
