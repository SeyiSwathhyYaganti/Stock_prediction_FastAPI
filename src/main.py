from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from models.model import load_model, predict

app = FastAPI()
model = load_model()
#Define the request model for input validation
class RequestBody(BaseModel):
    Adj_Close: float   # Adjusted Close price
    High: float        # High price
    Low: float        # Low price
    Open: float        # Open price
    Volume: int        # Volume
    Year: int        
    Month: int
    Day: int

#Endpoint to make predictions
@app.post("/predict")
def get_prediction(request: RequestBody):
    input_data= np.array([
        request.Adj_Close,
        request.High,
        request.Low,
        request.Open,
        request.Volume,
        request.Year,
        request.Month,
        request.Day
    ]).reshape(1,-1)

    print("Input data for prediction:", input_data)

    prediction = predict(input_data)
    print("prediction is:",prediction)

    return {"Stock prediction": float(prediction[0])}

# if __name__ == "__main__":
#     # Test the full preprocessing, training, and prediction flow
#     model = load_model()
#     test_data = {
#         "Year": 2024,
#         "Month": 9,
#         "Day": 26,
#         "Adj_Close": 100.0,
#         "High": 100.0,
#         "Low": 100.0,
#         "Open": 100.0,
#         "Volume": 1000000
#     }
#     test_input = pd.DataFrame([test_data])
#     print("Test input shape:", test_input.shape)
#     prediction = model.predict(test_input)
#     print("Prediction:", prediction)