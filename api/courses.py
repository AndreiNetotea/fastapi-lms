from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db
from pydantic_schemas.course import Course, CourseCreate, CourseUpdate
from api.utils.courses import (
    get_course,
    get_courses,
    create_course,
    update_course,
    delete_course,
)

router = fastapi.APIRouter()


@router.get("/courses", response_model=List[Course])
async def read_courses(db: AsyncSession = Depends(async_get_db)):
    courses = await get_courses(db=db)
    return courses


@router.post("/courses", response_model=Course, status_code=201)
async def create_new_course(
    course: CourseCreate, db: AsyncSession = Depends(async_get_db)
):
    new_course = await create_course(db=db, course=course)
    return new_course


@router.get("/courses/{course_id}", response_model=Course)
async def read_course(
    course_id: int, db: AsyncSession = Depends(async_get_db)
):
    db_course = await get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@router.put("/courses/{course_id}")
async def patch_course(
    course_id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(async_get_db),
):
    try:
        response = await update_course(
            db=db, course_id=course_id, course=course
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Something went wrong")
    if response is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return response


@router.delete("/courses/{course_id}", response_model=bool)
async def remove_course(
    course_id: int, db: AsyncSession = Depends(async_get_db)
):
    response = await delete_course(db=db, course_id=course_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return response
