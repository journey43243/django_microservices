from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer,String
from typing import List
from uuid import uuid4

class Base(DeclarativeBase):
    pass

class Users(Base):

    __tablename__ = "users"

    user_id_pk : Mapped[str] = mapped_column(primary_key = True, default = uuid4)
    username : Mapped[str] = mapped_column(String(32), nullable =False)
    password : Mapped[str] = mapped_column(String(256), nullable = False)
    email : Mapped[str] = mapped_column(String, nullable = False)
    permission_groupd_id = mapped_column(ForeignKey("permissions_groups.group_id_pk"))


class Permissions(Base):

    __tablename__ = "permissions"

    permission_id_pk : Mapped[int] = mapped_column(Integer,primary_key = True)
    group_id_fk = mapped_column(ForeignKey("permissions_groups.group_id_pk"))


class PermissionsGroups(Base):

    __tablename__ = "permissions_groups"

    group_id_pk : Mapped[int] = mapped_column(Integer, primary_key = True)
    group_name : Mapped[str] = mapped_column(String, unique = True)