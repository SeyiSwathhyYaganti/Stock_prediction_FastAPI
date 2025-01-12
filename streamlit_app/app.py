import streamlit as st
import requests

# Title of the app
st.title("Stock Price Prediction Model")

# Create input fields for the user to input data
year = st.number_input("Year", min_value=1900, value=2024)
month = st.number_input("Month", min_value=1, max_value=12, value= 9)
day = st.number_input("Day", min_value=1, max_value=31, value= 26)
adj_close = st.number_input("Adjusted Close", min_value=0.0, value=100.0)
high = st.number_input("High Price", min_value=0.0, value=100.0)
low = st.number_input("Low Price", min_value=0.0, value=100.0)
open_price = st.number_input("Open Price", min_value=0.0, value=100.0)
volume = st.number_input("Volume", min_value=0, value=1000000)

# Button to submit the data
if st.button("Submit"):
    # Create the payload
    payload = {
        "Year": int(year),
        "Month": int(month),
        "Day": int(day),
        "Adj_Close": float(adj_close),
        "High": float(high),
        "Low": float(low),
        "Open": float(open_price),
        "Volume": int(volume)
    }

    # Send the request to the FastAPI backend (or any other prediction service)
    response = requests.post("http://localhost:8000/predict", json=payload)

    # Display the response from the server
    if response.status_code == 200:
        st.success("Data submitted successfully!")
        result = st.json(response.json())  # Assuming the response contains the predicted price
        #result = response.json()
        #result = st.json(response.json())  
        #predicted_price = result.get("Stock prediction")
        #st.write("Predicted Stock Price: ", predicted_price)

    else:
        st.error(f"Error submitting data.{response.status_code} - {response.text}")
