from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db_setup import get_db
from app.jwt_utils import create_access_token
from app.models import UserModel
from app.schemas import RoleBase, Token
from app.utils import verify

auth_router = APIRouter(tags=["Authentication"])


@auth_router.post("/login", response_model=Token)
async def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    # q = (
    #     db.query(UserModel)
    #     .filter(UserModel.username == user_credentials.username)
    #     .filter(UserModel.is_active == True)
    # )
    user = (
        db.query(UserModel)
        .filter_by(username=user_credentials.username)
        .filter_by(is_active=True)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail={"msg": "Wrong Credentials"}
        )
    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail={"msg": "Wrong Credentials"}
        )

    return {
        "access_token": create_access_token(
            data={
                "user_id": user.id,
                "roles": [role.role_name for role in user.roles],
            }
        ),
        "token_type": "Bearer",
    }
