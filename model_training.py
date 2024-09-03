import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
import joblib
import os
import logging

# Setup logging configuration
logging.basicConfig(filename='training.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def load_preprocessed_data():
    """
    Load the preprocessed data for training and testing.
    """
    logging.info("Loading preprocessed training and testing data.")
    X_train = pd.read_csv('dataset/X_train.csv')
    X_test = pd.read_csv('dataset/X_test.csv')
    y_train = pd.read_csv('dataset/y_train.csv')
    y_test = pd.read_csv('dataset/y_test.csv')

    return X_train, X_test, y_train.values.ravel(), y_test.values.ravel()


def scale_data(X_train, X_test):
    """
    Standardize the data for better model performance.
    """
    logging.info("Standardizing the features for improved model performance.")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Save the scaler for future use
    joblib.dump(scaler, 'models/scaler.pkl')
    logging.info("Feature scaler saved as 'models/scaler.pkl'.")

    return X_train_scaled, X_test_scaled


def train_model(X_train, y_train, hyperparameter_tuning=False):
    """
    Train a RandomForestClassifier model, with optional hyperparameter tuning.
    """
    logging.info("Training the RandomForestClassifier model.")

    # Define the base model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    if hyperparameter_tuning:
        logging.info("Performing hyperparameter tuning using GridSearchCV.")
        # Define hyperparameter grid
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [10, 20, None],
            'min_samples_split': [2, 5, 10]
        }
        grid_search = GridSearchCV(
            estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
        grid_search.fit(X_train, y_train)
        model = grid_search.best_estimator_

        logging.info(f"Best hyperparameters found: {grid_search.best_params_}")

    else:
        model.fit(X_train, y_train)

    logging.info("Model training completed.")
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using accuracy, confusion matrix, and classification report.
    Save results to log and a separate file.
    """
    logging.info("Evaluating the trained model.")
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    # Log and print the evaluation results
    logging.info(f"Model Accuracy: {accuracy * 100:.2f}%")
    logging.info("\nConfusion Matrix:\n" + str(conf_matrix))
    logging.info("\nClassification Report:\n" + class_report)

    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print("\nConfusion Matrix:")
    print(conf_matrix)
    print("\nClassification Report:")
    print(class_report)

    # Save report to a file
    with open('results/evaluation_report.txt', 'w') as report_file:
        report_file.write(f"Model Accuracy: {accuracy * 100:.2f}%\n\n")
        report_file.write("Confusion Matrix:\n")
        report_file.write(str(conf_matrix) + "\n\n")
        report_file.write("Classification Report:\n")
        report_file.write(class_report)

    logging.info("Evaluation report saved to 'results/evaluation_report.txt'.")

    return accuracy


def save_model(model, model_path='models/supply_chain_model.pkl'):
    """
    Save the trained model to disk for later use.
    """
    joblib.dump(model, model_path)
    logging.info(f"Model saved to {model_path}")
    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    # Ensure results and models directories exist
    if not os.path.exists('results'):
        os.makedirs('results')
    if not os.path.exists('models'):
        os.makedirs('models')

    # Load preprocessed data
    X_train, X_test, y_train, y_test = load_preprocessed_data()

    # Scale the data
    X_train_scaled, X_test_scaled = scale_data(X_train, X_test)

    # Train the model with optional hyperparameter tuning
    model = train_model(X_train_scaled, y_train, hyperparameter_tuning=True)

    # Evaluate the model
    evaluate_model(model, X_test_scaled, y_test)

    # Save the trained model
    save_model(model)
