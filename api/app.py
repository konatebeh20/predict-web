# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_cors import CORS
# from flask_jwt_extended import JWTManager
# from routes.cancer_prediction import cancer_prediction_bp  # Importez votre blueprint ici

# # Création de l'application Flask
# app = Flask(__name__)

# # Configuration de la base de données SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Remplacez par l'URI de votre base de données
# app.config['SECRET_KEY'] = 'your_secret_key'  # Remplacez par une clé secrète sécurisée
# app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'  # Remplacez par une clé JWT sécurisée

# # Initialisation des extensions
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# cors = CORS(app)
# jwt = JWTManager(app)

# # Enregistrement des blueprints
# app.register_blueprint(cancer_prediction_bp, url_prefix='/api')

# # Import des modèles SQLAlchemy
# from models import PatientInfo, GenomicData, TranscriptomicData, ...  # Importez vos modèles ici

# if __name__ == '__main__':
#     app.run(debug=True)































from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.cancer_prediction import cancer_prediction_bp  # Importez votre blueprint ici

# Création de l'application Flask
app = Flask(__name__)

# Configuration de la base de données SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Remplacez par l'URI de votre base de données
app.config['SECRET_KEY'] = 'your_secret_key'  # Remplacez par une clé secrète sécurisée
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'  # Remplacez par une clé JWT sécurisée

# Initialisation des extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
cors = CORS(app)
jwt = JWTManager(app)

# Enregistrement des blueprints
app.register_blueprint(cancer_prediction_bp, url_prefix='/api')

# Import des modèles SQLAlchemy
from models import PatientInfo, GenomicData, TranscriptomicData, ...  # Importez vos modèles ici

if __name__ == '__main__':
    app.run(debug=True)
