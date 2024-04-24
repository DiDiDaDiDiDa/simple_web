#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :__init__.py
# @Time :2024/4/24 11:05
# @Author :WZY
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from . import user
