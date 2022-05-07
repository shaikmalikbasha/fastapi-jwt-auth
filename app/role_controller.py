from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db_setup import get_db
from app.models import RoleModel
from app.schemas import CreateAndUpdateRole, RoleResponse

router = APIRouter(prefix="/roles", tags=["User Routes"])


@router.get("/", response_model=List[RoleResponse])
async def get_users(db: Session = Depends(get_db)):
    return db.query(RoleModel).all()


@router.post("/")
async def get_users(
    user_input: dict = CreateAndUpdateRole, db: Session = Depends(get_db)
):
    print(f"Input Body: {user_input}")
    new_role = RoleModel(role_name=user_input["role_name"])

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return {"msg": "New role created", "created_role": new_role}
