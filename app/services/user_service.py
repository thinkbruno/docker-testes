import uuid
import bcrypt
from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def list_users(self):
        return self.repository.get_all()

    def get_user(self, user_id):
        user = self.repository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def create_user(self, name, email, password):

        if self.repository.get_by_email(email):
            raise ValueError("Email already exists")

        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        user = User(
            public_id=str(uuid.uuid4()),
            name=name,
            email=email,
            password=hashed.decode("utf-8"),
        )

        return self.repository.create(user)

    def update_user(self, user_id, data):
        user = self.get_user(user_id)

        if "email" in data and data["email"] != user.email:
            if self.repository.get_by_email(data["email"]):
                raise ValueError("Email already exists")

        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)

        if "password" in data:
            hashed = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
            user.password = hashed.decode("utf-8")

        return self.repository.update(user)

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        self.repository.delete(user)
