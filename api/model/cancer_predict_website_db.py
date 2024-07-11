from flask_sqlalchemy import SQLAlchemy
from config.db import *
# from datetime import datetime

class Clinician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(10))
    sex = db.Column(db.String(10))
    password = db.Column(db.String(60), nullable=False)
    predictions = db.relationship('Prediction', backref='clinician', lazy=True)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    # patient_id = db.Column(db.String(100))
    age = db.Column(db.String(10))
    sex = db.Column(db.String(10))
    symptoms = db.Column(db.String(255))
    test_results = db.Column(db.String(255))
    tumor_size = db.Column(db.Float)
    lymph_status = db.Column(db.String(50))
    estrogen_receptor = db.Column(db.String(50))
    progesterone_receptor = db.Column(db.String(50))
    her2_status = db.Column(db.String(50))
    gene1 = db.Column(db.String(100))
    gene2 = db.Column(db.String(100))
    protein1 = db.Column(db.String(100))
    protein2 = db.Column(db.String(100))
    protein3 = db.Column(db.String(100))
    protein4 = db.Column(db.String(100))
    protein5 = db.Column(db.String(100))
    specific_genes = db.Column(db.String(255))
    genomic_data_file = db.Column(db.String(255))
    bmi = db.Column(db.Float)
    vitamin_c = db.Column(db.Float)
    ki67 = db.Column(db.Float)
    cortisol = db.Column(db.Float)

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clinician_id = db.Column(db.Integer, db.ForeignKey('clinician.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    result = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
