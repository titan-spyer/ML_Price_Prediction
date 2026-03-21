import pandas as pd
from src.data_ingest import DataIngestFactory
# from zenml import step

# @step
def data_ingestion_step(file_path: str) -> pd.DataFrame:
    """Ingest data from a ZIP file using the appropriate DataIngestor."""
    # Determine the file extension
    # file_extension = ".zip"
    
    # Get the appropriate DataIngestor
    try:
        data_ingestor = DataIngestFactory.get_ingestor(".zip")
    except ValueError as e:
        print(f".zip failed as error {e}")

    try:
        data_ingestor = DataIngestFactory.get_ingestor("zip")
    except ValueError as e:
        print(f"zip failed as error {e}")
    
    # Ingest the data and load it into a DataFrame
    df = data_ingestor.ingest_data(file_path)
    return df