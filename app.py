from flask import Flask, request, jsonify, send_from_directory
import os
from Server.util import get_location_names, get_estimated_price, load_saved_artifacts

app = Flask(__name__, static_folder='Client')

# Initialize the model when the application starts
load_saved_artifacts()

@app.route('/')
def serve_client():
    return send_from_directory('Client', 'app.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('Client', path)

@app.route('/get_location_names', methods=['GET'])
def get_locations():
    response = jsonify({
        'locations': get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run() 