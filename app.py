from flask import Flask
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
load_dotenv(find_dotenv('.flaskenv'), override=True)

from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)


class Helloworld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(Helloworld, '/')

if __name__ == '__main__':
    app.run()
