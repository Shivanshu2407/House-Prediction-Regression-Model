from flask import Flask, request, jsonify, send_from_directory
import os
from Server.util import get_location_names, get_estimated_price, load_saved_artifacts
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='Client')

# Initialize the model when the application starts
logger.info("Starting application and loading artifacts...")
load_saved_artifacts()
logger.info("Artifacts loaded successfully")

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({"status": "healthy"}), 200

@app.route('/')
def serve_client():
    try:
        logger.info("Serving index page")
        return send_from_directory('Client', 'app.html')
    except Exception as e:
        logger.error(f"Error serving index page: {str(e)}")
        return jsonify({"error": "Failed to load page"}), 500

@app.route('/<path:path>')
def serve_static(path):
    try:
        logger.info(f"Serving static file: {path}")
        return send_from_directory('Client', path)
    except Exception as e:
        logger.error(f"Error serving static file {path}: {str(e)}")
        return jsonify({"error": "File not found"}), 404

@app.route('/get_location_names', methods=['GET'])
def get_locations():
    try:
        logger.info("Getting location names")
        locations = get_location_names()
        logger.info(f"Found {len(locations)} locations")
        response = jsonify({
            'locations': locations
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        logger.error(f"Error getting locations: {str(e)}")
        return jsonify({"error": "Failed to get locations"}), 500

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_price():
    try:
        logger.info("Received price prediction request")
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        logger.info(f"Predicting price for: {location}, {total_sqft} sqft, {bhk} BHK, {bath} bath")
        estimated_price = get_estimated_price(location, total_sqft, bhk, bath)
        logger.info(f"Estimated price: {estimated_price}")

        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        logger.error(f"Error predicting price: {str(e)}")
        return jsonify({"error": "Failed to predict price"}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 