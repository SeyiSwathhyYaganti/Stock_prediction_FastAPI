import pandas as pd
from config import Config
from sklearn.model_selection import train_test_split

def load_data():
    data = pd.read_csv(Config.DATA_PATH)
    print(data.dtypes) #All the data is in Object data type. we should convert it into int and float
    return data

def drop_rows(data): #dropping 2nd and 3rd rows which has unwanted details
    data = data.drop(index = [0,1])
    print(data.head())
    return data

def clean_columns(data):
    data.columns = ["Date","Adj_Close", "Close", "High", "Low", "Open", "Volume"]
    print(data.head())
    return data

def parse_dates(data):
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Year"] = data["Date"].dt.year
    data["Month"] = data["Date"].dt.month
    data["Day"] = data["Date"].dt.day
    data = data.drop(columns=["Date"])  # Drop the original Date column
    print("Data after parsing dates:\n", data.head())
    print(data.dtypes)
    return data

def convert_dtype(data):
    columns_to_convert = ["Adj_Close", "Close", "High", "Low", "Open", "Volume"]
    # Apply pd.to_numeric to each specified column with errors='coerce'
    data[columns_to_convert] = data[columns_to_convert].apply(pd.to_numeric, errors='coerce')
    print("After conversion:\n",data.dtypes)
    print(data.head())
    return data

def split_data(data):
    X = data.drop(["Close"], axis=1)
    y = data["Close"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=Config.TEST_SIZE, random_state=Config.RANDOM_SEED)
    print("training data:\n",X_train)
    print("training data target:\n", y_train)

    print("Feature columns in X_train:", X_train.columns)

    return X_train, X_test, y_train, y_test

def preprocess_data():
    """Full preprocessing pipeline."""
    # data = load_data()
    # data = drop_rows(data)  
    # data = clean_columns(data)
    # data = parse_dates(data)

    data = (load_data()
            .pipe(drop_rows)
            .pipe(clean_columns)
            .pipe(parse_dates)
            .pipe(convert_dtype))
            
    return data

if __name__ == "__main__":
    processed_data = preprocess_data()
    X_train, X_test, y_train, y_test = split_data(processed_data)
    print("Data preprocessed and split successfully!")

