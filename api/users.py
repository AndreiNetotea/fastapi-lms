from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db
from pydantic_schemas.user import UserCreate, User, UserUpdate
from pydantic_schemas.course import Course
from api.utils.users import (
    get_user,
    get_user_by_email,
    get_users,
    create_user,
    delete_user,
    update_user,
)
from api.utils.courses import get_user_courses

# from sqlalchemy.orm import Session

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(async_get_db)
):
    users = await get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(
    user: UserCreate, db: AsyncSession = Depends(async_get_db)
):
    db_user = await get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Email is already registered"
        )
    new_user = await create_user(db=db, user=user)
    return new_user


@router.get("/users/{user_id}", response_model=User)
async def get_user_by_id(
    user_id: int, db: AsyncSession = Depends(async_get_db)
):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/{user_id}/courses", response_model=List[Course])
async def read_user_courses(
    user_id: int, db: AsyncSession = Depends(async_get_db)
):
    courses = await get_user_courses(db=db, user_id=user_id)
    return courses


@router.put("/users/{user_id}")
async def patch_user(
    user_id: int, user: UserUpdate, db: AsyncSession = Depends(async_get_db)
):
    response = await update_user(db=db, user_id=user_id, user=user)
    if response is None:
        raise HTTPException(status_code=404, detail="User not found")
    return response


@router.delete("/users/{user_id}", response_model=bool)
async def remove_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    response = await delete_user(db=db, user_id=user_id)
    if response is None:
        raise HTTPException(status_code=404, detail="User not found")
    return response
