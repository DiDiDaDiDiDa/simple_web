#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :Helloworld.py
# @Time :2024/4/24 11:24
# @Author :WZY
from flask_restful import Resource

from api import api


class Helloworld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(Helloworld, '/hello')