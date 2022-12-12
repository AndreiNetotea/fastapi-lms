from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing courses and students",
    version="0.1.0",
    contact={
        "name": "Andrei",
        "email": "andrei.netotea@gmail.com"
    },
    license_info={
        "name": "MIT",
    }
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model=List[User])
async def get_user():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully"}

@app.get("/users/{user_id}")
async def get_user(
    user_id: int = Path(..., description="The ID of the user to get"),
    q: str = Query(None, max_length=5)
):
    return {"user": users[user_id], "query": q}