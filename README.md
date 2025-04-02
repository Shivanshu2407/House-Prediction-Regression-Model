# House Price Prediction Web Application

A machine learning-based web application that predicts house prices based on various features. The application is deployed on Render.

## Features

- House price prediction using machine learning
- Interactive web interface
- RESTful API endpoint for predictions
- Health check endpoint for monitoring
- Comprehensive logging system

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-learn
- **Deployment**: Render

## Project Structure

```
house-prediction/
├── app.py                 # Main Flask application
├── model.py              # Machine learning model implementation
├── static/              # Static files (CSS, JS)
├── templates/           # HTML templates
├── requirements.txt     # Python dependencies
└── .env                # Environment variables
```

## Prerequisites

- Python 3.10.13 or higher
- pip (Python package manager)
- Git (for version control)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd house-prediction
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with the following variables:
```
APP_URL=https://your-app-url.onrender.com
```

## Running the Application

Start the Flask application:
```bash
python app.py
```

The application will be available at `http://localhost:5000` (or your configured port).

## API Endpoints

### Health Check
- **URL**: `/health`
- **Method**: GET
- **Response**: `{"status": "healthy"}`

### Prediction
- **URL**: `/predict`
- **Method**: POST
- **Request Body**: JSON with house features
- **Response**: Predicted house price

## Deployment

The application is configured for deployment on Render with:
- Python 3.10.13 runtime
- Automatic service monitoring
- Health check endpoint

### Deployment Steps
1. Push your code to a Git repository
2. Connect your repository to Render
3. Configure the following environment variables:
   - `APP_URL`: Your application's URL
   - `PYTHON_VERSION`: 3.10.13

## Monitoring and Logs

- Application logs are stored in `app.log`
- Health check endpoint provides service status

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the maintainers.

## Acknowledgments

- Flask framework
- Scikit-learn library
- Render hosting platform
- Contributors and maintainers 