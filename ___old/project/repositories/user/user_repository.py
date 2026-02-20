# PEP8 OK
# -*- coding: utf-8 -*-
from peewee import *
from project.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    id = AutoField(null=False)
    public_id = CharField()
    name = CharField()
    email = CharField()
    password = CharField()
    is_active = BooleanField()

    class Meta:
        table_name = 'user'
