# PEP8 OK
# -*- coding: utf-8 -*-
import logging
import traceback
from array import *

from flask import jsonify, make_response
from project.config import Server
from project.framework.exception.exceptions import (BusinessException,
                                                    NotAuthorizedException)


class BaseService():
    logged_user = None

    def __init__(self, accessData=None):
        logging.basicConfig(filename='api.log', level=logging.DEBUG)

        if accessData:
            self.set_logged_user(accessData)

    def return_success(self, message, details):
        if message is None:
            message = 'Ok'
        return make_response(jsonify({'code': 200, 'message': message, 'details': details}), 200)

    def return_exception(self, ex):
        http_code = 400
        if isinstance(ex, BusinessException):
            exception = {
                'message': ex.message
            }
        elif isinstance(ex, NotAuthorizedException):
            http_code = 401
            exception = {
                'message': ex.message
            }
        else:
            http_code = 500
            exception = {
                'message': [str(x) for x in ex.args]
            }
        logging.debug(traceback.format_exc())
        __return = {'code': http_code, 'message': exception["message"]}
        print(Server().SERVER_DEBUG)
        if Server().SERVER_DEBUG == "True":
            __return['traceback'] = traceback.format_exc()
        return make_response(jsonify(__return), http_code)
