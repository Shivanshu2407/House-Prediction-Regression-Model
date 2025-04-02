import pickle
import json
import numpy as np
import os
from sklearn.linear_model import LinearRegression

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    # Since we're using a dummy model, return a basic estimate
    # This is just a placeholder - in a real application, we would use the trained model
    base_price = sqft * 0.45  # base price calculation
    bhk_factor = bhk * 5      # adjustment for number of bedrooms
    bath_factor = bath * 3    # adjustment for number of bathrooms
    location_factor = 0       # location premium
    
    if location.lower() in ["1st block jayanagar", "1st phase jp nagar", "2nd phase jp nagar", "electronic city"]:
        location_factor = 10  # premium locations
    
    estimated_price = (base_price + bhk_factor + bath_factor + location_factor)
    return round(estimated_price, 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations
    global __model

    try:
        # Get the absolute path to the artifacts directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        artifacts_path = os.path.join(os.path.dirname(current_dir), 'artifacts', 'columns.json')
        
        with open(artifacts_path, "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    except Exception as e:
        print(f"Error loading columns.json: {e}")
        # Default columns if file is not available
        __data_columns = ["total_sqft", "bath", "bhk", "1st block jayanagar", "1st phase jp nagar", "2nd phase jp nagar", "electronic city"]
        __locations = __data_columns[3:]

    # Instead of loading from pickle, create a new model
    __model = LinearRegression()
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location