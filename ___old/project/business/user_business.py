# PEP8 OK
# -*- coding: utf-8 -*-

import uuid

from project.framework.exception.exceptions import BusinessException
from project.repositories.user.user_repository import UserRepository
from werkzeug.security import generate_password_hash


class UserBusiness():

    def search_all(self):
        try:
            users = list(UserRepository().select(
                UserRepository.public_id,
                UserRepository.name,
                UserRepository.email).where(
                UserRepository.is_active == True).dicts())
            return users
        except:
            raise BusinessException('Nenhum usuário encontrado')

    def search_specific(self, public_id):
        try:
            user = UserRepository().select().where(
                UserRepository.public_id == public_id).first()
            return user
        except:
            raise BusinessException('Usuário não encontrado')

    def add(self, body):
        try:
            data = {
                "public_id": str(uuid.uuid4()),
                "name": str(body['name']).encode('utf8'),
                "email": str(body["email"]),
                "password": self.hash_password(body["password"]) if "password" in body else None
            }
            UserRepository().create(**data)
            return ('Usuário adicionado!')
        except:
            raise BusinessException('Erro ao adicionar usuário')

    def update(self, user, body):
        try:
            if 'status' in body:
                user.is_active = body["status"]
            if 'password' in body:
                user.password = self.hash_password(body["password"])
            user.save()
            return ('Usuário atualizado!')
        except:
            raise BusinessException('Erro ao atualizar usuário')

    def delete(self, user):
        try:
            user.delete_instance()
            return ('Usuário deletado!')
        except:
            raise BusinessException('Erro ao deletar usuário')

    def hash_password(self, password):
        try:
            hashed = generate_password_hash(
                password.encode('utf8'), method="sha1")
            return hashed
        except:
            raise BusinessException('Senha não informada')
