# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from sqlalchemy import delete as sqlalchemy_delete
# from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.orm import Session

from db.models.module import Module
from pydantic_schemas.module import ModuleCreate, ModuleUpdate


# async def get_module(db: AsyncSession, module_id: int):
#     query = select(Module).where(Module.id == module_id)
#     result = await db.execute(query)
#     return result.scalar_one_or_none()


# async def get_modules(db: AsyncSession, skip: int = 0, limit: int = 100):
#     query = select(Module).offset(skip).limit(limit)
#     modules = await db.execute(query)
#     return modules.scalars().all()


# async def create_module(db: AsyncSession, module: ModuleCreate):
#     db_module = Module(**module.dict())
#     async with db.begin():
#         db.add(db_module)
#         try:
#             await db.commit()
#         except Exception:
#             await db.rollback()
#             return None
#     await db.refresh(db_module)
#     return db_module


# async def delete_module(db: AsyncSession, module_id: int):
#     query = sqlalchemy_delete(Module).where(Module.id == module_id)
#     await db.execute(query)
#     try:
#         await db.commit()
#     except Exception:
#         await db.rollback()
#         return None
#     return True


# async def update_module(
#     db: AsyncSession, module_id: int, module: ModuleUpdate
# ):
#     query = (
#         sqlalchemy_update(Module)
#         .where(Module.id == module_id)
#         .values(module.dict())
#         .execution_options(
#             synchronize_session="fetch"
#         )
#     )

#     await db.execute(query)
#     try:
#         await db.commit()
#     except Exception:
#         await db.rollback()
#         raise
#     return await get_module(db, module_id=module_id)


def create_module(db: Session, module: ModuleCreate):
    db_user = Module(**module.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_module(db: Session, module_id: int):
    return db.query(Module).filter(Module.id == module_id).first()


def get_modules(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Module).offset(skip).limit(limit).all()


def delete_module(db: Session, module_id: int):
    db.query(Module).filter(Module.id == module_id).delete()
    db.commit()
    return True


def update_module(db: Session, module_id: int, module: ModuleUpdate):
    db.query(Module).filter(Module.id == module_id).update(module.dict())
    db.commit()
    return get_module(db, module_id=module_id)
