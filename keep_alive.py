import requests
import time
import logging
from datetime import datetime
import os
from dotenv import load_dotenv
from urllib.parse import urljoin

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('keep_alive.log'),
        logging.StreamHandler()
    ]
)

# Get the app URL from environment variable or use default
APP_URL = os.getenv('APP_URL', 'https://house-prediction-regression-model.onrender.com').rstrip('/')
HEALTH_ENDPOINT = urljoin(APP_URL + '/', 'health')
PING_INTERVAL = 180  # 3 minutes in seconds
MAX_RETRIES = 3
RETRY_DELAY = 10  # seconds

def test_connection():
    """Test the initial connection and verify the health endpoint."""
    try:
        response = requests.get(HEALTH_ENDPOINT, timeout=30)
        logging.info(f"Initial connection test - Status: {response.status_code}")
        logging.info(f"Response content: {response.text}")
        return response.status_code == 200
    except requests.RequestException as e:
        logging.error(f"Initial connection test failed: {str(e)}")
        return False

def ping_app():
    """Send a ping request to the application with retries."""
    for attempt in range(MAX_RETRIES):
        try:
            logging.info(f"Sending ping to: {HEALTH_ENDPOINT}")
            response = requests.get(HEALTH_ENDPOINT, timeout=30)
            response_text = response.text
            logging.info(f"Response content: {response_text}")
            
            if response.status_code == 200:
                logging.info(f"Ping successful - Status: {response.status_code}")
                return True
            else:
                logging.warning(f"Attempt {attempt + 1}/{MAX_RETRIES} - Status code: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"Attempt {attempt + 1}/{MAX_RETRIES} - Request failed: {str(e)}")
        
        if attempt < MAX_RETRIES - 1:
            logging.info(f"Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
    
    return False

def main():
    """Main function to run the keep-alive service."""
    logging.info(f"Starting keep-alive service")
    logging.info(f"App URL: {APP_URL}")
    logging.info(f"Health endpoint: {HEALTH_ENDPOINT}")
    logging.info(f"Ping interval: {PING_INTERVAL} seconds")
    
    # Test initial connection
    if not test_connection():
        logging.error("Initial connection test failed. Please check the URL and endpoint.")
        logging.info("Continuing anyway...")
    
    failures = 0
    max_consecutive_failures = 5
    
    while True:
        try:
            if ping_app():
                if failures > 0:
                    logging.info(f"Connection restored after {failures} failures")
                failures = 0
            else:
                failures += 1
                logging.error(f"Ping failed. Consecutive failures: {failures}")
                
                if failures >= max_consecutive_failures:
                    logging.critical(f"Too many consecutive failures ({failures}). Please check the application.")
            
            # Wait for the next interval
            time.sleep(PING_INTERVAL)
            
        except KeyboardInterrupt:
            logging.info("Keep-alive service stopped by user")
            break
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            time.sleep(PING_INTERVAL)

if __name__ == "__main__":
    main() 