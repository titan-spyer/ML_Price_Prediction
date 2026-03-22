import logging
import mlflow
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def model_building_step(X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
    """
    Builds and trains a Linear Regression model using scikit-learn wrapped in a pipeline.
    """
    # Ensure the inputs are of the correct type
    if not isinstance(X_train, pd.DataFrame):
        raise TypeError("X_train must be a pandas DataFrame.")
    if not isinstance(y_train, pd.Series):
        raise TypeError("y_train must be a pandas Series.")

    # Identify categorical and numerical columns
    categorical_cols = X_train.select_dtypes(include=["object", "category"]).columns
    numerical_cols = X_train.select_dtypes(exclude=["object", "category"]).columns

    logging.info(f"Categorical columns: {categorical_cols.tolist()}")
    logging.info(f"Numerical columns: {numerical_cols.tolist()}")

    # Define preprocessing for categorical and numerical features
    numerical_transformer = SimpleImputer(strategy="mean")

    # Define preprocessing for categorical Data
    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    # Bundle preprocessing for numerical and categorical data
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numerical_transformer, numerical_cols),
            ("cat", categorical_transformer, categorical_cols),
        ]
    )

    # Define the model training pipeline
    pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", LinearRegression())])

    # Start an MLflow run to log the model training process
    mlflow.set_experiment("House Price Prediction")

    with mlflow.start_run():
        try:
            # Enable autologging for capture metrics unit
            mlflow.sklearn.autolog()

            logging.info("Building and training the Linear Regression model.")
            pipeline.fit(X_train, y_train)
            logging.info("Model training completed.")
            
        except Exception as e:
            logging.error(f"Error during model training: {e}")
            raise e

    return pipeline

if __name__ == "__main__":
    pass