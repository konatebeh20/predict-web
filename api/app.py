from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    patient_id = db.Column(db.String(100))
    age = db.Column(db.Integer)
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

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(**data)
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added successfully!'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
