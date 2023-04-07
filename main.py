from fastapi import FastAPI

from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing courses and students",
    version="0.1.0",
    contact={"name": "Andrei", "email": "andrei.netotea@gmail.com"},
    license_info={
        "name": "MIT",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
