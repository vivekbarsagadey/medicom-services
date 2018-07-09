from flask_restful import Resource, Api


class HomeController(Resource):
    def get(self):
        return {'hello': 'home'}