# PEP8 OK
# -*- coding: utf-8 -*-
import os


class Server:

    BASE_PATH = "/"
    API_VERSION = "v1"
    SERVER_DEBUG = os.getenv("SERVER_DEBUG", True)

    MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "bd-testes")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "12345")
    MYSQL_PORT = os.getenv("MYSQL_PORT", 3307)

    def get_base_path(self):
        return self.BASE_PATH + self.API_VERSION
