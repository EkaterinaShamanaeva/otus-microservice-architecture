from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.db.crud.user import UserCRUD
from app.db.exceptions import CRUDError, UserNotFoundError
from app.schemas.user import UserCreate

app = FastAPI()


@app.get("/health/")
async def health_check():
    return {"status": "OK"}


@app.post("/users/")
def create_user(user: UserCreate, session: Session = Depends(get_db)):
    try:
        user = UserCRUD(session).create_user(name=user.name, email=user.email)
        return user
    except CRUDError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/users/")
def get_users(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    user = UserCRUD(session).get_users(skip=skip, limit=limit)
    return user


@app.get("/users/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_db)):
    user = UserCRUD(session).get_user(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate, session: Session = Depends(get_db)):
    try:
        user = UserCRUD(session).update_user(user_id=user_id, name=user.name, email=user.email)
        return user
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail="User not found")
    except CRUDError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_db)):
    try:
        UserCRUD(session).delete_user(user_id=user_id)
        return {"message": "User deleted successfully"}
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail="User not found")
    except CRUDError as e:
        raise HTTPException(status_code=400, detail=str(e))
