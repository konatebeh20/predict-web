# Importation des modules nécessaires
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db  # Importez db depuis votre application Flask (assurez-vous que db est bien initialisé dans app.py)


# Initialisation de l'application Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Chemin de votre base de données
db = SQLAlchemy(app)

# Modèle pour les informations personnelles
class PatientInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    tumor_size = db.Column(db.Float)
    other_variables = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
# class ClinicalData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     sex = db.Column(db.String(10), nullable=False)
#     date_of_birth = db.Column(db.Date, nullable=False)
#     tumor_size = db.Column(db.String(20), nullable=False)
#     other_variables = db.Column(db.Text, nullable=True)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Modèle pour les données multi-omiques
# class GenomicData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     patient_id = db.Column(db.Integer, db.ForeignKey('patient_info.id'), nullable=False)
#     # Define other fields related to genomic data
#     # Example: data_file_path = db.Column(db.String(100), nullable=False)
#     # Example: analysis_result = db.Column(db.String(100))
    
# Modèle pour les données multi-omiques
class MultiOmicsData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genomic_data = db.Column(db.String(100), nullable=True)
    transcriptomic_data = db.Column(db.String(100), nullable=True)
    metabolomic_data = db.Column(db.String(100), nullable=True)
    proteomic_data = db.Column(db.String(100), nullable=True)
    epigenomic_data = db.Column(db.String(100), nullable=True)
    microbiomic_data = db.Column(db.String(100), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Route pour gérer la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données du formulaire
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    sex = request.form.get('sex')
    date_of_birth = request.form.get('date_of_birth')
    tumor_size = request.form.get('tumor_size')
    other_variables = request.form.get('other_variables')

    # Enregistrer les données cliniques dans la base de données
    clinical_data = clinical_data(first_name=first_name, last_name=last_name, sex=sex,
                                 date_of_birth=date_of_birth, tumor_size=tumor_size,
                                 other_variables=other_variables)
    db.session.add(clinical_data)
    db.session.commit()

    # Enregistrer les données multi-omiques dans la base de données
    genomic_data = request.files['genomic_data']
    transcriptomic_data = request.files['transcriptomiques_data']
    metabolomic_data = request.files['metabolomiques_data']
    proteomic_data = request.files['proteomiques_data']
    epigenomic_data = request.files['epigenomiques_data']
    microbiomic_data = request.files['microbiomiquees_data']

    # Enregistrer les chemins des fichiers ou les données dans la base de données
    multiomics_data = MultiOmicsData(genomic_data=genomic_data, transcriptomic_data=transcriptomic_data,
                                    metabolomic_data=metabolomic_data, proteomic_data=proteomic_data,
                                    epigenomic_data=epigenomic_data, microbiomic_data=microbiomic_data)
    db.session.add(multiomics_data)
    db.session.commit()

    # Logique de prédiction ici (à remplacer par votre code de prédiction)

    # Retourner une réponse JSON pour afficher ou traiter les résultats côté frontend
    return jsonify({'message': 'Prediction successful!', 'status': 'success'})

    # Define relationship to PatientInfo model
    # patient = db.relationship('PatientInfo', backref=db.backref('genomic_data', lazy=True))

if __name__ == '__main__':
    app.run(debug=True)
