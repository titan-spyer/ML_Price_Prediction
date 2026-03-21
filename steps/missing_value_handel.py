import pandas as pd
from src.handeling_misssing_values import MissingValueHandlerContext, DropMissingValues, FillMissingValues
# from zenml import step

# @step
def handle_missing_values_step(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """Handles missing values using MissingValueHandler and the specified strategy."""
    if strategy == "drop":
        handler = MissingValueHandlerContext(DropMissingValues(axis=0))
    elif strategy in ["mean", "median", "mode", "constant"]:
        handler = MissingValueHandlerContext(FillMissingValues(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value handling strategy: {strategy}")

    cleaned_df = handler.handle_missing_values(df)
    return cleaned_df