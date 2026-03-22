from steps.data_ingestion import data_ingestion_step
from steps.missing_value_handel import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step
from steps.outlier_detection_step import outlier_detection_step
from steps.data_splitter_step import data_splitter_step
from steps.model_building_step import model_building_step
# from zenml import pipeline, step, Model


# @pipeline(
#     model = Model(
#         name = "prices_predictor"
#     ),
# )
def ml_pipeline():
    """Define an end-to-end machine learning pipeline."""

    # Data Ingestion Step
    raw_data = data_ingestion_step(
        file_path = "Data.zip"
    )
    
    # Handling Missing Values Step
    filled_data = handle_missing_values_step(raw_data)

    # Feature Engineering Step
    transformed_data = feature_engineering_step(
        filled_data, strategy="log", features=["Gr Liv Area", "SalePrice"]
    )
    
    # Outlier Detection Step
    outlier_data = outlier_detection_step(transformed_data, column_name="SalePrice")

    # Data Splitting Step
    x_train, x_test, y_train, y_test = data_splitter_step(outlier_data, target_column="SalePrice")

    # Model Building step
    model = model_building_step(x_train, y_train)

    
    return model


if __name__ == "__main__":
    # Running the pipeline
    run = ml_pipeline()
    print("Pipeline executed successfully.")
    print(run.head())