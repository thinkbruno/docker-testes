# PEP8 OK
# -*- coding: utf-8 -*-
import datetime

from peewee import Model, MySQLDatabase
from project.config import Server

mysql_db = MySQLDatabase(Server().MYSQL_DATABASE, user=Server(
).MYSQL_USER, password=Server().MYSQL_PASSWORD, host=Server().MYSQL_HOST, port=int(Server().MYSQL_PORT))


class BaseRepository(Model):

    class Meta:
        database = mysql_db

    def prepare_update_params(self, params):
        for key, value in params.items():
            if not key == 'created_at' or not key == 'updated_at':
                setattr(self, key, value)

    def save(self, *args, **kwargs):
        if self._pk is None:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super(BaseRepository, self).save(*args, **kwargs)
