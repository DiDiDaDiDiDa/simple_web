#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :user.py.py
# @Time :2024/4/24 14:46
# @Author :WZY
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api
from api.common.external_api import res
from api.models.user import UserModel


class UserService(Resource):
    @jwt_required()
    def get(self):
        userList = UserModel.get_all_user()
        result = []
        for user in userList:
            result.append(user.dict())

        return res(data=result)


api.add_resource(UserService, '/getUserList')
