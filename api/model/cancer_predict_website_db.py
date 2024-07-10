from flask_sqlalchemy import SQLAlchemy
from config.db import *
# from datetime import datetime


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