from typing import Optional

from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    user_id: int
    description: Optional[str] = None
    module: Optional[int]


class CourseCreate(CourseBase):
    ...


class CourseUpdate(CourseBase):
    ...


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True
