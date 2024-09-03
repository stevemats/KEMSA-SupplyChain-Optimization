import os
import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(file_path):
    """
    Load the dataset from a CSV file into a pandas DataFrame.

    Parameters:
    - file_path: str, the path to the CSV file containing the dataset.

    Returns:
    - data: pd.DataFrame, the loaded dataset.

    Raises:
    - FileNotFoundError: if the file does not exist.
    - ValueError: if the file is empty or cannot be parsed.
    """
    try:
        data = pd.read_csv(file_path)
        if data.empty:
            raise ValueError("The dataset is empty.")
        print("Data loaded successfully!")
        return data
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
        raise
    except pd.errors.EmptyDataError as ede:
        print(f"Error: The file is empty or unreadable: {ede}")
        raise
    except Exception as e:
        print(f"Error loading data: {e}")
        raise


def preprocess_data(data):
    """
    Preprocess the dataset by handling missing values, encoding categorical variables,
    and preparing features (X) and target (y) variables.

    Parameters:
    - data: pd.DataFrame, the raw dataset to preprocess.

    Returns:
    - X: pd.DataFrame, the feature matrix after preprocessing.
    - y: pd.Series, the target variable (Restock_Flag).
    """
    print("Starting data preprocessing...")

    # Handle missing values by filling with 0 (can adjust this strategy if needed)
    data.fillna(0, inplace=True)
    print(
        f"Missing values handled. Number of rows with missing data: {data.isnull().sum().sum()}")

    # Encode categorical variables using one-hot encoding
    categorical_columns = ['Region', 'Supply_Category', 'Month']
    data_encoded = pd.get_dummies(
        data, columns=categorical_columns, drop_first=True)
    print(f"Categorical variables encoded. New shape: {data_encoded.shape}")

    # Split the dataset into features (X) and target (y)
    X = data_encoded.drop(['Restock_Flag'], axis=1)
    y = data_encoded['Restock_Flag']
    print(
        f"Features and target separated. Feature matrix shape: {X.shape}, Target shape: {y.shape}")

    return X, y


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.

    Parameters:
    - X: pd.DataFrame, the feature matrix.
    - y: pd.Series, the target variable.
    - test_size: float, the proportion of data to use as test set.
    - random_state: int, the seed for reproducibility.

    Returns:
    - X_train: pd.DataFrame, the training feature matrix.
    - X_test: pd.DataFrame, the testing feature matrix.
    - y_train: pd.Series, the training target variable.
    - y_test: pd.Series, the testing target variable.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)
    print(
        f"Data split completed. Train shape: {X_train.shape}, Test shape: {X_test.shape}")
    return X_train, X_test, y_train, y_test


def save_preprocessed_data(X_train, X_test, y_train, y_test, output_dir='./dataset/'):
    """
    Save preprocessed data into CSV files for later use.

    Parameters:
    - X_train: pd.DataFrame, training feature matrix.
    - X_test: pd.DataFrame, testing feature matrix.
    - y_train: pd.Series, training target variable.
    - y_test: pd.Series, testing target variable.
    - output_dir: str, the directory where preprocessed data will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    X_train.to_csv(f'{output_dir}/X_train.csv', index=False)
    X_test.to_csv(f'{output_dir}/X_test.csv', index=False)
    y_train.to_csv(f'{output_dir}/y_train.csv', index=False)
    y_test.to_csv(f'{output_dir}/y_test.csv', index=False)

    print(f"Preprocessed data saved successfully to {output_dir}")


if __name__ == "__main__":
    # Load raw data
    data = load_data('./dataset/supply-data.csv')

    # If data is successfully loaded, preprocess it
    if data is not None:
        X, y = preprocess_data(data)

        # Split the preprocessed data into training and testing sets
        X_train, X_test, y_train, y_test = split_data(X, y)

        # Save the preprocessed data
        save_preprocessed_data(X_train, X_test, y_train, y_test)
