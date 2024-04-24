#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :logout.py.py
# @Time :2024/4/24 14:42
# @Author :WZY
from flask_jwt_extended import jwt_required, get_jwt
from flask_restful import Resource

from api import api
from api.common.external_api import res
from api.models.revoked_token import RevokedTokenModel


class Logout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        try:
            # 用户退出系统时 将 token 加入黑名单
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return res()
        except:
            return res(success=False, message='服务器繁忙！', code=500)


api.add_resource(Logout, '/logout')