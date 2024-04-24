#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :user.py
# @Time :2024/4/24 11:47
# @Author :WZY
import uuid

from flask import request
from flask_restful import Resource
from ..models.user import UserModel

from api import api


class User(Resource):
    def post(self):
        username=request.json.get('username')
        pwd=request.json.get('password')
        salt=uuid.uuid4().hex
        userModel = UserModel(username= username,pwd= pwd,salt=salt)
        userModel.addUser()

        return 'success'


api.add_resource(User, '/user')