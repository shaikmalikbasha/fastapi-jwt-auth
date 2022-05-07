from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db_setup import get_db
from app.models import UserHasRole, UserModel
from app.schemas import CreateAndUpdateUser, UserResponse
from app.utils import get_hash_password
from app.jwt_utils import get_current_user

router = APIRouter(prefix="/users", tags=["User Routes"])


@router.get("/", response_model=List[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    users_sql = db.query(UserModel).filter_by(is_active=True)
    print(users_sql)
    users = users_sql.all()
    print(users)
    return users


@router.post("/")
async def get_users(
    user_input: dict = CreateAndUpdateUser, db: Session = Depends(get_db)
):
    print(f"Input Body: {user_input}")
    user_input["password"] = get_hash_password(user_input["password"])
    new_user = UserModel(
        full_name=user_input["full_name"],
        username=user_input["username"],
        password=user_input["password"],
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "New user created", "created_user": new_user}


@router.get("/{user_id}/roles/{role_id}")
async def add_role_to_user(user_id: int, role_id: int, db: Session = Depends(get_db)):
    user_role = UserHasRole(user_id=user_id, role_id=role_id)
    db.add(user_role)
    db.commit()
    db.refresh(user_role)

    return user_role
