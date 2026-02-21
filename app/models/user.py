from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    public_id = Column(String(45), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)
    is_active = Column(Boolean, default=True)
