from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreateSchema, UserUpdateSchema

user_bp = Blueprint("users", __name__, url_prefix="/users")

service = UserService()
create_schema = UserCreateSchema()
update_schema = UserUpdateSchema()


@user_bp.get("/")
def list_users():
    users = service.list_users()
    return jsonify(
        [
            {
                "id": u.id,
                "public_id": u.public_id,
                "name": u.name,
                "email": u.email,
                "is_active": u.is_active,
            }
            for u in users
        ]
    )


@user_bp.get("/<int:user_id>")
def get_user(user_id):
    try:
        user = service.get_user(user_id)
        return jsonify(
            {
                "id": user.id,
                "public_id": user.public_id,
                "name": user.name,
                "email": user.email,
                "is_active": user.is_active,
            }
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@user_bp.post("/")
def create_user():
    try:
        data = create_schema.load(request.json)
        user = service.create_user(**data)

        return (
            jsonify(
                {
                    "id": user.id,
                    "public_id": user.public_id,
                    "name": user.name,
                    "email": user.email,
                }
            ),
            201,
        )

    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@user_bp.put("/<int:user_id>")
def update_user(user_id):
    try:
        data = create_schema.load(request.json)  # PUT exige tudo
        user = service.update_user(user_id, data)

        return jsonify({"id": user.id, "name": user.name, "email": user.email})

    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@user_bp.patch("/<int:user_id>")
def patch_user(user_id):
    try:
        data = update_schema.load(request.json)
        user = service.update_user(user_id, data)

        return jsonify({"id": user.id, "name": user.name, "email": user.email})

    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@user_bp.delete("/<int:user_id>")
def delete_user(user_id):
    try:
        service.delete_user(user_id)
        return jsonify({"message": "User deleted"}), 204

    except ValueError as e:
        return jsonify({"error": str(e)}), 404
