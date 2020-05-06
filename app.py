from flask import Flask, jsonify, request, make_response
import requests

app = Flask(__name__)

# /api/virufy -> all data will be posted here and we will return the response

@app.route('/api/virufy', methods=['POST'])
def post():
    age = request.form.get('age')
    gender = request.form.get('gender')
    smoker = request.form.get('smoker')
    symptoms = request.form.getlist('reported_symptoms')
    medical_history = request.form.getlist('medical_history')
    # cough audio = request.form.get('')
    # breath audio = request.form.get('')
    # finger video = request.form.get('')
    patient_location = request.form.get('location')

    response = {"age": age, "gender": gender,
     "smoker": smoker, "reported_symptoms": symptoms,
     "medical_history": medical_history,
     "location": patient_location }

    return make_response(jsonify(response), 200)

app.run(port=5000, debug=True)
