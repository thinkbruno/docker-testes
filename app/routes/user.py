from flask import Blueprint, jsonify, request

user_bp = Blueprint("user", __name__, url_prefix="/users")

# Fake in-memory list (para testar rápido)
USERS = []


@user_bp.get("/")
def list_users():
    return jsonify(USERS)


@user_bp.post("/")
def create_user():
    data = request.json
    USERS.append(data)
    return jsonify({"message": "User created"}), 201
