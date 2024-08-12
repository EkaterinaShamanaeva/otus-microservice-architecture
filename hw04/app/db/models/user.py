from sqlalchemy import Column, Integer, String, Table

from app.db.base import Base, metadata, engine


# SQLAlchemy модель для таблицы пользователей
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)


# Создание таблицы пользователей
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String, unique=True)
)

metadata.create_all(engine)
