#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :__init__.py
# @Time :2024/4/24 11:16
# @Author :WZY

from flask import Blueprint

from api.common.external_api import ExternalApi

bp=Blueprint('api',__name__, url_prefix='/v1')

api=ExternalApi(bp)

from .resources import Helloworld,user


