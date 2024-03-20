from sqlalchemy.exc import SQLAlchemyError

from app.db.exceptions import CRUDError, UserNotFoundError
from app.db.models.user import User


class UserCRUD:

    def __init__(self, session):
        self.session = session

    def create_user(self, name: str, email: str):
        try:
            user = User(name=name, email=email)
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except SQLAlchemyError as e:
            self.session.rollback()
            raise CRUDError

    def get_user(self, user_id: int):
        user = self.session.query(User).filter(User.id == user_id).first()
        return user

    def get_users(self, skip: int, limit: int):
        users = self.session.query(User).offset(skip).limit(limit).all()
        return users

    def update_user(self, user_id: int, name: str, email: str):
        user = self.get_user(user_id=user_id)
        if user is None:
            raise UserNotFoundError
        try:
            user.name = name
            user.email = email
            self.session.commit()
            self.session.refresh(user)
            return user
        except SQLAlchemyError as e:
            self.session.rollback()
            raise CRUDError

    def delete_user(self, user_id: int):
        user = self.get_user(user_id=user_id)
        if user is None:
            raise UserNotFoundError
        try:
            self.session.delete(user)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise CRUDError
