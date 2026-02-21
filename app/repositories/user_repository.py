from app.database import SessionLocal
from app.models.user import User


class UserRepository:

    def get_all(self):
        with SessionLocal() as session:
            return session.query(User).all()

    def get_by_id(self, user_id):
        with SessionLocal() as session:
            return session.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email):
        with SessionLocal() as session:
            return session.query(User).filter(User.email == email).first()

    def create(self, user):
        with SessionLocal() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def update(self, user):
        with SessionLocal() as session:
            session.merge(user)
            session.commit()
            return user

    def delete(self, user):
        with SessionLocal() as session:
            session.delete(user)
            session.commit()
