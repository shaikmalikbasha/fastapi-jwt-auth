from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Text)
from sqlalchemy.orm import relationship

from app.db_setup import Base


class UserHasRole(Base):
    __tablename__ = "user_has_roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    username = Column(Text, nullable=False, index=True, unique=True)
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)

    roles = relationship(
        "RoleModel", secondary=UserHasRole.__table__, back_populates="users"
    )


class RoleModel(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    users = relationship(
        "UserModel", secondary=UserHasRole.__table__, back_populates="roles"
    )
