#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :config.py
# @Time :2024/4/24 10:21
# @Author :WZY
import os
from datetime import timedelta

# 数据库相关配置
MYSQL_USER_NAME=os.getenv('MYSQL_USER_NAME')
MYSQL_USER_PASSWORD=os.getenv('MYSQL_USER_PASSWORD')
MYSQL_HOSTNAME=os.getenv('MYSQL_HOSTNAME')
MYSQL_PORT=os.getenv('MYSQL_PORT')
MYSQL_DATABASE_NAME=os.getenv('MYSQL_DATABASE_NAME')

class Config:
    Debug = False
    Testing=False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER_NAME}:{MYSQL_USER_PASSWORD}@{MYSQL_HOSTNAME}:{MYSQL_PORT}/{MYSQL_DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_BLOCKLIST_TOKEN_CHECKS = ['access']


class DevConfig(Config):
    DEBUG = True

class ProductConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True

config={
    'dev':DevConfig,
    'product':ProductConfig,
    'testing':TestingConfig
}