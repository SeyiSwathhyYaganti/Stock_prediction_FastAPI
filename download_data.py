import yfinance as yf
import os

def fetch_and_save_data(ticker = "^GSPC", start_date = "1975-01-01", end_date = "2024-05-01", folder = "data"):
    #Ensure the data folder exists
    os.makedirs(folder, exist_ok=True)

    #download data
    data = yf.download(ticker, start=start_date, end=end_date)

    #define file path
    file_path = os.path.join(folder, f"s&p500_data.csv")

    #save data to csv
    data.to_csv(file_path)
    print(f"Data saved to {file_path}")

if __name__ =="__main__":
    fetch_and_save_data()