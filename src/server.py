from flask import Flask
from flask_restful import Api
#from flask_restful_swagger_2 import Api
from werkzeug.contrib.fixers import ProxyFix
from flask_cors import CORS
from com.medicom.core.web.home import HomeController
from com.medicom.health.diabetes.web.diabetes import DiabetesController, DiabetesDataSetController
app = Flask(__name__)
CORS(app)

api = Api(app , catch_all_404s=True)
#api = Api(app,api_version='0.0', api_spec_url='/api/swagger')


api.add_resource(HomeController, '/', endpoint="home")
api.add_resource(DiabetesController, '/api/diabetes/<model_name>', endpoint="diabetes")
api.add_resource(DiabetesDataSetController, '/api/diabetes/dataset/<name>', endpoint="diabetes/dataset")

if __name__ == '__main__':
    app.run(debug=True)