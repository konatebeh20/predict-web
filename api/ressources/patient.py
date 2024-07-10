from helpers.patient import *
from flask_restful import Resource

class PatientsApi(Resource):
    def post(self,route):
        if route == 'createPatient':
            return createPatient()


