from pydantic import BaseModel


# Pydantic модель для валидации входящих данных при создании пользователя
class UserCreate(BaseModel):
    name: str
    email: str
