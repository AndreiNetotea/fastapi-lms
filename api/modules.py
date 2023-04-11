from typing import List

import fastapi
from fastapi import Depends, HTTPException

# from sqlalchemy.ext.asyncio import AsyncSession

# from db.db_setup import async_get_db

from pydantic_schemas.module import ModuleCreate, ModuleUpdate, Module

from api.utils.modules import (
    get_module,
    get_modules,
    create_module,
    delete_module,
    update_module,
)
from sqlalchemy.orm import Session
from db.db_setup import get_db

router = fastapi.APIRouter()


# @router.get("/modules", response_model=List[Module])
# async def read_modules(
#     skip: int = 0, limit: int = 100, db: AsyncSession = Depends(async_get_db)
# ):
#     modules = await get_modules(db, skip=skip, limit=limit)
#     return modules


# @router.post("/modules", response_model=Module, status_code=201)
# async def create_new_module(
#     module: ModuleCreate, db: AsyncSession = Depends(async_get_db)
# ):
#     try:
#         new_module = await create_module(db=db, module=module)
#         return new_module
#     finally:
#         await db.close()


# @router.get("/modules/{module_id}", response_model=Module)
# async def get_module_by_id(
#     module_id: int, db: AsyncSession = Depends(async_get_db)
# ):
#     db_module = await get_module(db=db, module_id=module_id)
#     if db_module is None:
#         raise HTTPException(status_code=404, detail="Module not found")
#     return db_module


# @router.put("/modules/{module_id}")
# async def patch_module(
#     module_id: int, module: ModuleUpdate,
#     db: AsyncSession = Depends(async_get_db)
# ):
#     response = await update_module(db=db, module_id=module_id, module=module)
#     if response is None:
#         raise HTTPException(status_code=404, detail="Module not found")
#     return response


# @router.delete("/modules/{module_id}", response_model=bool)
# async def remove_module(
#     module_id: int, db: AsyncSession = Depends(async_get_db)
# ):
#     response = await delete_module(db=db, module_id=module_id)
#     if response is None:
#         raise HTTPException(status_code=404, detail="Module not found")
#     return response


@router.get("/modules", response_model=List[Module])
async def read_modules(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    modules = get_modules(db, skip=skip, limit=limit)
    return modules


@router.post("/modules", response_model=Module, status_code=201)
async def create_new_module(
    module: ModuleCreate, db: Session = Depends(get_db)
):
    return create_module(db=db, module=module)


@router.put("/modules/{module_id}", response_model=Module, status_code=201)
async def patch_module(
    module_id: int, module: ModuleUpdate, db: Session = Depends(get_db)
):
    return update_module(db=db, module_id=module_id, module=module)


@router.get("/modules/{module_id}", response_model=Module)
async def get_module_by_id(module_id: int, db: Session = Depends(get_db)):
    return get_module(db=db, module_id=module_id)


@router.delete("/modules/{module_id}", response_model=bool)
async def remove_module(module_id: int, db: Session = Depends(get_db)):
    module = get_module(db=db, module_id=module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return delete_module(db=db, module_id=module_id)
