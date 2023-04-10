# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy import update as sqlalchemy_update

from db.models.user import User
from pydantic_schemas.user import UserCreate, UserUpdate


async def get_user(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_user_by_email(db: AsyncSession, email: str):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(User).offset(skip).limit(limit)
    users = await db.execute(query)
    return users.scalars().all()


async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        return None
    await db.refresh(db_user)
    return db_user


async def delete_user(db: AsyncSession, user_id: int):
    query = sqlalchemy_delete(User).where(User.id == user_id)
    await db.execute(query)
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        return None
    return True


async def update_user(db: AsyncSession, user_id: int, user: UserUpdate):
    query = (
        sqlalchemy_update(User)
        .where(User.id == user_id)
        .values(user.dict())
        .execution_options(synchronize_session="fetch")
    )

    await db.execute(query)
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
    return await get_user(db, user_id=user_id)


#  The Sync version of this of users utils.

# def get_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()

# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(User).offset(skip).limit(limit).all()


# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()


# def create_user(db: Session, user: UserCreate):
#     db_user = User(email=user.email, role=user.role)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
