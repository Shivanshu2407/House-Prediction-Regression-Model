import requests
import time
import logging
from datetime import datetime
import os
from dotenv import load_dotenv

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
APP_URL = os.getenv('APP_URL', 'https://house-prediction-regression-model.onrender.com/')
HEALTH_ENDPOINT = f"{APP_URL}/health"
PING_INTERVAL = 300  # 5 minutes in seconds
MAX_RETRIES = 3
RETRY_DELAY = 10  # seconds

def ping_app():
    """Send a ping request to the application with retries."""
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(HEALTH_ENDPOINT, timeout=30)
            if response.status_code == 200:
                logging.info(f"Ping successful - Status: {response.status_code}")
                return True
            else:
                logging.warning(f"Attempt {attempt + 1}/{MAX_RETRIES} - Unexpected status code: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"Attempt {attempt + 1}/{MAX_RETRIES} - Request failed: {str(e)}")
        
        if attempt < MAX_RETRIES - 1:
            logging.info(f"Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
    
    return False

def main():
    """Main function to run the keep-alive service."""
    logging.info(f"Starting keep-alive service for {APP_URL}")
    logging.info(f"Ping interval: {PING_INTERVAL} seconds")
    
    failures = 0
    max_consecutive_failures = 5
    
    while True:
        try:
            if ping_app():
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