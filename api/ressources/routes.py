from flask import Blueprint, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from model.cancer_predict_website_db import Patient, db
from datetime import datetime


# Création d'un Blueprint pour les routes
cancer_prediction_bp = Blueprint('cancer_prediction', __name__)

# Route pour la page de prédiction (prediction)
@cancer_prediction_bp.route('/prediction', methods=['POST'])
def predict_cancer():
    # Extract data from request
    # first_name = request.form.get('first_name')
    # last_name = request.form.get('last_name')
    # sex = request.form.get('sex')
    # date_of_birth = request.form.get('date_of_birth')
    # tumor_size = request.form.get('tumor_size')
    # other_variables = request.form.get('other_variables')

    # Process data (implement your cancer prediction logic here)

    # Dummy response for demonstration
    prediction_result = {
        'message': 'Cancer prediction logic goes here'
    }

    return jsonify(prediction_result)

# Route pour ajouter un patient
@cancer_prediction_bp.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(**data)
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added successfully!'})

# Route pour prédire le cancer
@cancer_prediction_bp.route('/predict', methods=['POST'])
def predict_cancer():
    # Code de prédiction du cancer ici
    return jsonify({'message': 'Cancer prediction logic goes here'})

# Route pour la page d'accueil (home)
@cancer_prediction_bp.route('/')
@cancer_prediction_bp.route('/home')
def home():
    return render_template('home.html')

# Route pour la page À propos (about)
@cancer_prediction_bp.route('/about')
def about():
    return render_template('about.html')

# Route pour la page de contact (contact)
@cancer_prediction_bp.route('/contact')
def contact():
    return render_template('contact.html')

# Exemple de route pour recevoir des données POST
# @cancer_prediction_bp.route('/patients', methods=['POST'])
# def add_patient():
#     data = request.get_json()
#     # Create new patient using your models
#     new_patient = Patient(**data)
#     # Add patient to database session
#     db.session.add(new_patient)
#     db.session.commit()
#     return jsonify({'message': 'Patient added successfully!'})


# Exemple de gestion d'une page d'erreur 404
@cancer_prediction_bp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Endpoint pour la racine des URL
@cancer_prediction_bp.route('/<path:dummy>')
def fallback(dummy):
    return render_template('404.html'), 404
