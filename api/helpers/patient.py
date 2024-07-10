from flask import request
from model.cancer_predict_website_db import Patient
from config.db import db
from config.constant import *


def createPatient():
    new_patient = Patient()

    new_patient.name = request.json.get('name')
    new_patient.age = request.json.get('age')
    new_patient.sex = request.json.get('sex')
    new_patient.symptoms = request.json.get('symptoms')
    new_patient.test_results = request.json.get('test_results')
    new_patient.tumor_size = request.json.get('tumor_size')
    new_patient.lymph_status = request.json.get('lymph_status')
    new_patient.estrogen_receptor = request.json.get('estrogen_receptor')
    new_patient.progesterone_receptor = request.json.get('progesterone_receptor')
    new_patient.her2_status = request.json.get('her2_status')
    new_patient.gene1 = request.json.get('gene1')
    new_patient.gene2 = request.json.get('gene2')
    new_patient.protein1 = request.json.get('protein1')
    new_patient.protein2 = request.json.get('protein2')
    new_patient.protein3 = request.json.get('protein3')
    new_patient.protein4 = request.json.get('protein4')
    new_patient.protein5 = request.json.get('protein5')
    new_patient.specific_genes = request.json.get('specific_genes')
    new_patient.genomic_data_file = request.json.get('genomic_data_file')
    new_patient.bmi = request.json.get('bmi')
    new_patient.vitamin_c = request.json.get('vitamin_c')
    new_patient.ki67 = request.json.get('ki67')
    new_patient.cortisol = request.json.get('cortisol')
    
    
    db.session.add(new_patient)
    db.session.commit()
    
    return True