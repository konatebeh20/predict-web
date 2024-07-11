from helpers.patient import *
from flask_restful import Resource

class ClinicianApi(Resource):
    def post(self,route):
        if route == 'createClinician':
            return createClinician()
