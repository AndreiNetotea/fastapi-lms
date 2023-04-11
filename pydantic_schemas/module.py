from datetime import datetime

from pydantic import BaseModel


class ModuleBase(BaseModel):
    name: str
    description: str


class ModuleCreate(ModuleBase):
    ...


class ModuleUpdate(ModuleBase):
    ...


class Module(ModuleBase):
    id: int
    users: list[int]
    courses: list[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
