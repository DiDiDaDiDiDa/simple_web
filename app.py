import os

from flask import Flask
from dotenv import load_dotenv, find_dotenv

from api.models import db
from config import config
from manage import migrate

# 导入环境变量
load_dotenv(find_dotenv())
load_dotenv(find_dotenv('.flaskenv'), override=True)

from flask_restful import Api, Resource


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    return app


app = create_app(os.getenv('Flask_ENV', 'dev'))
api = Api(app)


class Helloworld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(Helloworld, '/')

if __name__ == '__main__':
    app.run()
