#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :register.py.py
# @Time :2024/4/24 14:25
# @Author :WZY

import uuid

from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash

from api import api
from api.common.external_api import res
from api.models.user import UserModel


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        reg_args_valid(parser)
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return res(success=False, message="Repeated username!", code=400)
        else:
            try:
                data['salt'] = uuid.uuid4().hex
                data['pwd'] = generate_password_hash('{}{}'.format(data['salt'], data['pwd']))
                user = UserModel(**data)
                user.addUser()
                return res(message="Register succeed!")
            except Exception as e:
                return res(success=False, message="Error: {}".format(e), code=500)


def reg_args_valid(parser):
    parser.add_argument('username', type=str, location='json')
    parser.add_argument('password', type=str, dest='pwd', location='json')


api.add_resource(Register, '/register')
