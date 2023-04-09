# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy import update as sqlalchemy_update

from db.models.course import Course
from pydantic_schemas.course import CourseCreate, CourseUpdate


async def get_course(db: AsyncSession, course_id: int):
    query = select(Course).where(Course.id == course_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_courses(db: AsyncSession):
    query = select(Course)
    courses = await db.execute(query)
    return courses.scalars().all()


async def get_user_courses(db: AsyncSession, user_id: int):
    query = select(Course).where(Course.user_id == user_id)
    result = await db.execute(query)
    return result.scalars().all()


async def create_course(db: AsyncSession, course: CourseCreate):
    db_course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id,
    )
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course


async def update_course(
    db: AsyncSession, course_id: int, course: CourseUpdate
):
    query = (
        sqlalchemy_update(Course)
        .where(Course.id == course_id)
        .values(course.dict())
        .execution_options(synchronize_session="fetch")
    )

    await db.execute(query)
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        return None
    return await get_course(db, course_id=course_id)


async def delete_course(db: AsyncSession, course_id: int):
    query = sqlalchemy_delete(Course).where(Course.id == course_id)
    await db.execute(query)
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        return None
    return True


#  The Sync version of this of coursers utils.

# def get_course(db: Session, course_id: int):
#     return db.query(Course).filter(Course.id == course_id).first()


# def get_courses(db: Session):
#     return db.query(Course).all()


# def get_user_courses(db: Session, user_id: int):
#     courses = db.query(Course).filter(Course.user_id == user_id).all()
#     return courses


# def create_course(db: Session, course: CourseCreate):
#     db_course = Course(
#         title=course.title,
#         description=course.description,
#         user_id=course.user_id,
#     )
#     db.add(db_course)
#     db.commit()
#     db.refresh(db_course)
#     return db_course
