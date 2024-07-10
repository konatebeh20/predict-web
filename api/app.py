# from flask import Flask, request, jsonify, render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model.cancer_predict_website_db import db, Patient
from ressources.patient import PatientsApi
# from ressources.routes import cancer_prediction_bp as routes_bp
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:souris_123@localhost/cancer_prediction_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
# db.init_app(app)
Migrate = Migrate(app, db)


# Enregistre le Blueprint pour les routes de prédiction du cancer
app.register_blueprint(PatientsApi, url_prefix='/')


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
    # app.register_blueprint(routes_bp, url_prefix='/')

