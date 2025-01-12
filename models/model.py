import xgboost as xgb
import joblib
import os
import pandas as pd
from config import Config
from src.preprocessing import load_data, preprocess_data, split_data
import logging

logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log format
)

def create_model():

    model= xgb.XGBRegressor(n_estimators= Config.N_ESTIMATORS, 
                            learning_rate= Config.LEARNING_RATE, 
                            max_depth= Config.MAX_DEPTH,
                            random_state = Config.RANDOM_SEED)
    return model

def train_model(model,X_train,y_train):
    model.fit(X_train, y_train)
    return model

def save_model(model):
    joblib.dump(model,Config.MODEL_PATH)

def load_model():
    if not os.path.exists(Config.MODEL_PATH):
        logging.info("Model file not found. Training model...")
        try:
            data = load_data()
            processed_data = preprocess_data()
            X_train, X_test, y_train, y_test = split_data(processed_data)
            model = create_model()
            model = train_model(model, X_train, y_train)
            save_model(model)
        except Exception as e:
            logging.error(f"Error during model training: {e}")
            raise ValueError("Model training failed.")
    else:
        logging.info("Model file found. Loading model...")
    
    try:
        model = joblib.load(Config.MODEL_PATH)
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        raise ValueError("Model loading failed.")
    
    return model

def predict(input_data):
    column_names = ["Adj_Close", "High", "Low", "Open", "Volume","Year", "Month", "Day"]
    input_data = pd.DataFrame(input_data, columns=column_names)
    model = load_model()
    prediction = model.predict(input_data)
    return prediction        