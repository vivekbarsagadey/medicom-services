from flask_restful import Resource
from com.medicom.health.diabetes.model.models import AllModels
from com.medicom.health.diabetes.model.k_nearest_neighbors import KNearestNeighborsModel
from com.medicom.health.diabetes.services.data_handler import DiabetesDataSet


class DiabetesController(Resource):
    '''@swagger.doc({
        'tags': ['DiabetesController'],
        'description': 'Returns a Diabetes data',
        'parameters': [
            {
                'model_name': 'all',
                'description': 'which model is going to use'
            }
        ],
        'responses': {
            '200': {
                'description': 'User',
                'examples': {
                    'application/json': {
                        'data': 'all'
                    }
                }
            }
        }
    })'''
    def get(self, model_name = "all"):
        if model_name == 'knn':
            return KNearestNeighborsModel().predict()
        else:
            return AllModels().predict()


class DiabetesDataSetController(Resource):
    def get(self , name = "header"):
        if name == 'header':
            return DiabetesDataSet().getColumns()
        elif name == 'shape' :
            return DiabetesDataSet().getDataShape()
        elif name == 'describe' :
            return DiabetesDataSet().getDescribe()
        elif name == 'data' :
            return DiabetesDataSet().getData()
        else:
            return DiabetesDataSet().getData()
