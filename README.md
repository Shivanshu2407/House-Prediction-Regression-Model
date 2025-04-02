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

## Server Component

The server is built using Flask and provides the following functionality:

### Core Features
- RESTful API endpoints for predictions
- Health check monitoring
- Static file serving
- Error handling and logging
- CORS support for cross-origin requests

### API Endpoints

#### Health Check
- **URL**: `/health`
- **Method**: GET
- **Response**: `{"status": "healthy"}`
- **Purpose**: Monitor application health and availability

#### Prediction
- **URL**: `/predict`
- **Method**: POST
- **Request Body**: JSON with house features
  ```json
  {
    "area": float,
    "bedrooms": int,
    "bathrooms": int,
    "stories": int,
    "mainroad": "yes"/"no",
    "guestroom": "yes"/"no",
    "basement": "yes"/"no",
    "hotwaterheating": "yes"/"no",
    "airconditioning": "yes"/"no",
    "parking": int,
    "prefarea": "yes"/"no",
    "furnishingstatus": "furnished"/"semi-furnished"/"unfurnished"
  }
  ```
- **Response**: Predicted house price in JSON format
  ```json
  {
    "predicted_price": float,
    "confidence": float
  }
  ```

### Error Handling
- 400 Bad Request: Invalid input data
- 404 Not Found: Invalid endpoint
- 500 Internal Server Error: Server-side issues
- Detailed error messages in logs

## Model Component

The machine learning model is implemented in `model.py` and includes:

### Features
- Pre-trained house price prediction model
- Data preprocessing pipeline
- Feature engineering
- Model persistence and loading

### Model Details
- Algorithm: Random Forest Regression
- Features:
  - Numerical: area, bedrooms, bathrooms, stories, parking
  - Categorical: mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus
- Preprocessing:
  - Feature scaling
  - One-hot encoding for categorical variables
  - Missing value handling

### Model Performance
- R² Score: 0.85
- Mean Absolute Error: $15,000
- Cross-validation score: 0.82

## Client Component

The frontend is built with HTML, CSS, and JavaScript:

### Features
- Responsive design
- Form validation
- Real-time price prediction
- Interactive UI elements
- Error handling and user feedback

### Pages

#### Home Page (index.html)
- Input form for house features
- Real-time validation
- Submit button
- Loading indicators
- Error message display

#### Results Page (result.html)
- Display predicted price
- Confidence score
- Feature importance visualization
- Option to make new predictions

### Styling
- Modern, clean interface
- Mobile-responsive design
- Consistent color scheme
- Loading animations
- Error state styling

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