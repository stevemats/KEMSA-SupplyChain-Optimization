# data_preparation.py

import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(file_path):
    """
    Loads the dataset from a CSV file and returns it as a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def preprocess_data(data):
    """
    Preprocesses the dataset by handling missing values, encoding categorical variables, and
    preparing features and target variables.
    """
    # Fill missing values (if any)
    data.fillna(0, inplace=True)

    # Encode categorical variables
    data_encoded = pd.get_dummies(
        data, columns=['Region', 'Supply_Category', 'Month'], drop_first=True)

    # Split features and target
    # Features (all except target)
    X = data_encoded.drop(['Restock_Flag'], axis=1)
    y = data_encoded['Restock_Flag']  # Target variable

    return X, y


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Splits the data into training and testing sets.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    # Load and preprocess data
    data = load_data('./dataset/supply-data.csv')

    if data is not None:
        X, y = preprocess_data(data)
        X_train, X_test, y_train, y_test = split_data(X, y)

        # Save the preprocessed data for model training
        X_train.to_csv('dataset/X_train.csv', index=False)
        X_test.to_csv('dataset/X_test.csv', index=False)
        y_train.to_csv('dataset/y_train.csv', index=False)
        y_test.to_csv('dataset/y_test.csv', index=False)
