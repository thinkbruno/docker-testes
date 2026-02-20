# PEP8 OK
# -*- coding: utf-8 -*-
from playhouse.shortcuts import model_to_dict
from project.business.user_business import UserBusiness

from .base_service import BaseService


class UserService(BaseService):

    def search_all(self):
        try:
            result = UserBusiness().search_all()
            return self.return_success("Sucesso", result)
        except Exception as ex:
            return self.return_exception(ex)

    def search_specific(self, public_id):
        try:
            result = UserBusiness().search_specific(public_id)
            __return = self.format_body(model_to_dict(result))
            return self.return_success("Sucesso", __return)
        except Exception as ex:
            return self.return_exception(ex)

    def add(self, body):
        try:
            result = UserBusiness().add(body)
            return self.return_success("Sucesso", result)
        except Exception as ex:
            return self.return_exception(ex)

    def update(self, public_id, body):
        try:
            user_business = UserBusiness()
            user = user_business.search_specific(public_id)
            result = user_business.update(user, body)
            return self.return_success("Sucesso", result)
        except Exception as ex:
            return self.return_exception(ex)

    def delete(self, public_id):
        try:
            user_business = UserBusiness()
            user = user_business.search_specific(public_id)
            result = user_business.delete(user)
            return self.return_success("Sucesso", result)
        except Exception as ex:
            return self.return_exception(ex)

    def format_body(self, body):
        __body = {
            "public_id": body["public_id"],
            "name": body["name"],
            "email": body["email"],
            "status": "Ativo" if body["is_active"] == True else "Inativo",
        }
        return __body
