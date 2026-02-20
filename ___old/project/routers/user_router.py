# PEP8 OK
# -*- coding: utf-8 -*-
import json

from flask import Blueprint, request
from project.config import Server
from project.services.user_service import UserService

user_route = Blueprint("user_route", __name__)

server = Server()
basePath = server.get_base_path()
USER_PREFIX = basePath + "/user"


@user_route.route(USER_PREFIX + "/", methods=["GET"])
def search_all():
    result = UserService().search_all()
    return result


@user_route.route(USER_PREFIX + "/<public_id>", methods=["GET"])
def search_specific(public_id):
    result = UserService().search_specific(public_id)
    return result


@user_route.route(USER_PREFIX + "/", methods=["POST"])
def add():
    params = json.loads(request.data)
    result = UserService().add(params)
    return result


@user_route.route(USER_PREFIX + "/<public_id>", methods=["PUT"])
def update(public_id):
    params = json.loads(request.data)
    result = UserService().update(public_id, params)
    return result


@user_route.route(USER_PREFIX + "/<public_id>", methods=["PATCH"])
def set_status(public_id):
    params = json.loads(request.data)
    result = UserService().update(public_id, params)
    return result


@user_route.route(USER_PREFIX + "/<public_id>", methods=["DELETE"])
def delete(public_id):
    result = UserService().delete(public_id)
    return result
