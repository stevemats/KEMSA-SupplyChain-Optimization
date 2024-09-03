import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import os


def load_model(model_path='models/supply_chain_model.pkl'):
    """
    Load the trained machine learning model from disk.
    """
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print(f"Model loaded from {model_path}\n")
        return model
    else:
        raise FileNotFoundError(f"Model not found at {model_path}")


def load_scaler(scaler_path='models/scaler.pkl'):
    """
    Load the scaler used during model training.
    """
    if os.path.exists(scaler_path):
        scaler = joblib.load(scaler_path)
        print(f"Scaler loaded from {scaler_path}\n")
        return scaler
    else:
        raise FileNotFoundError(f"Scaler not found at {scaler_path}")


def load_test_data(X_test_path='dataset/X_test.csv', y_test_path='dataset/y_test.csv'):
    """
    Load the test dataset for evaluation.
    """
    if os.path.exists(X_test_path) and os.path.exists(y_test_path):
        X_test = pd.read_csv(X_test_path)
        y_test = pd.read_csv(y_test_path)
        print(
            f"Test data loaded successfully from {X_test_path} and {y_test_path}\n")
        return X_test, y_test.values.ravel()
    else:
        raise FileNotFoundError("Test dataset not found!")


def predict_and_evaluate(model, X_test, y_test):
    """
    Use the trained model to make predictions and evaluate its performance.
    """
    print("Running predictions and evaluating model performance...")
    y_pred = model.predict(X_test)

    # Confusion matrix with heatmap
    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.title("Confusion Matrix", fontsize=16)
    plt.xlabel("Predicted", fontsize=12)
    plt.ylabel("Actual", fontsize=12)
    plt.show()

    # Classification report
    report = classification_report(y_test, y_pred)
    print("\nClassification Report:")
    print(report)

    # Log report to a file
    with open('results/classification_report.txt', 'w') as f:
        f.write("Classification Report\n")
        f.write(report)

    print("\nReport saved to 'results/classification_report.txt'\n")

    return y_pred


def plot_feature_importance(model, X_test):
    """
    Plot feature importance from a model, particularly useful for RandomForest or tree-based models.
    """
    if hasattr(model, 'feature_importances_'):
        importance = model.feature_importances_
        features = X_test.columns

        plt.figure(figsize=(10, 6))
        sns.barplot(x=importance, y=features, palette="viridis")
        plt.title("Feature Importance", fontsize=16)
        plt.xlabel("Importance Score", fontsize=12)
        plt.ylabel("Features", fontsize=12)
        plt.tight_layout()
        plt.show()
    else:
        print("Feature importance not available for this model.")


def generate_insights(X_test, y_pred):
    """
    Generate actionable insights by decoding one-hot encoded columns and filtering for restock-needed regions.
    """
    print("Generating actionable insights from the predictions...\n")

    # Combine predictions with test data
    restock_data = X_test.copy()
    restock_data['Predicted_Restock'] = y_pred

    # Decode 'Region' from one-hot encoding
    region_columns = [
        col for col in restock_data.columns if col.startswith('Region_')]
    restock_data['Region'] = restock_data[region_columns].idxmax(
        axis=1).str.replace('Region_', '')

    # Decode 'Medical_Supply' from one-hot encoding
    supply_columns = [
        col for col in restock_data.columns if col.startswith('Supply_Category_')]
    restock_data['Medical_Supply'] = restock_data[supply_columns].idxmax(
        axis=1).str.replace('Supply_Category_', '')

    # Filter for regions that require restocking
    restock_needed = restock_data[restock_data['Predicted_Restock'] == 1]

    # Display actionable insights
    if not restock_needed.empty:
        print("\nRegions and Medical Supplies Needing Restocking:\n")
        print(
            restock_needed[['Region', 'Medical_Supply', 'Predicted_Restock']])

        # Save insights to a file
        restock_needed[['Region', 'Medical_Supply', 'Predicted_Restock']].to_csv(
            'results/restock_insights.csv', index=False)
        print("\nRestock insights saved to 'results/restock_insights.csv'\n")
    else:
        print("\nNo regions require restocking based on the predictions.\n")


if __name__ == "__main__":
    # Ensure results directory exists
    if not os.path.exists('results'):
        os.makedirs('results')

    # Load the trained model
    model = load_model()

    # Load the scaler
    scaler = load_scaler()

    # Load the test data
    X_test, y_test = load_test_data()

    # Apply the scaler to the test data
    X_test_scaled = scaler.transform(X_test)

    # Predict and evaluate the model
    y_pred = predict_and_evaluate(model, X_test_scaled, y_test)

    # Plot feature importance
    plot_feature_importance(model, X_test)

    # Generate actionable insights
    generate_insights(X_test, y_pred)
