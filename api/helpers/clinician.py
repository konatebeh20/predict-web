from flask import request
from model.cancer_predict_website_db import Patient
from config.db import db
from config.constant import *

def createClinician():
    new_clinician = Clinician()

    new_clinician.name = request.json.get('name')
    new_clinician.age = request.json.get('age')
    new_clinician.sex = request.json.get('sex')
    new_clinician.password = request.json.get('password')

    db.session.add(new_clinician)
    db.session.commit()

    return True
