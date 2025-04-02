import requests
import logging
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_health_endpoint():
    """Test the health endpoint of the application."""
    base_url = "https://house-prediction-regression-model.onrender.com"
    health_url = urljoin(base_url.rstrip('/') + '/', 'health')
    
    logging.info(f"Testing connection to: {health_url}")
    
    try:
        # Test the health endpoint
        response = requests.get(health_url, timeout=30)
        logging.info(f"Status Code: {response.status_code}")
        logging.info(f"Response Content: {response.text}")
        
        # Test the main page
        main_response = requests.get(base_url, timeout=30)
        logging.info(f"Main page status code: {main_response.status_code}")
        
        return response.status_code == 200
    except requests.RequestException as e:
        logging.error(f"Connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    result = test_health_endpoint()
    if result:
        logging.info("✅ Connection test successful!")
    else:
        logging.error("❌ Connection test failed!") 