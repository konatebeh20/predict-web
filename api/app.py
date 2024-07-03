from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.cancer_prediction import cancer_prediction_bp  # Import blueprint

# Create Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Replace with your actual database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'  # Replace with a secure JWT secret key

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
cors = CORS(app)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(cancer_prediction_bp, url_prefix='/api')

# Import models
from models import PatientInfo, GenomicData, TranscriptomicData, ...  # Import your models

if __name__ == '__main__':
    app.run(debug=True)
