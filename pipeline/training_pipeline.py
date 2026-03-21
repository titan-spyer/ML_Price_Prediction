from steps.data_ingestion import data_ingestion_step
from steps.missing_value_handel import handle_missing_values_step
from zenml import pipeline, step, Model


@pipeline(
    model = Model(
        name = "prices_predictor"
    ),
)
def ml_pipeline():
    """Define an end-to-end machine learning pipeline."""

    # Data Ingestion Step
    raw_data = data_ingestion_step(
        file_path = "/content/ML_Price_Prediction/Data.zip"
    )
    
    # Handling Missing Values Step
    filled_data = handle_missing_values_step(raw_data)
    
    return filled_data


if __name__ == "__main__":
    # Running the pipeline
    run = ml_pipeline()