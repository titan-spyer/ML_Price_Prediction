from abc import ABC, abstractmethod

import pandas as pd


# Abstract Base Class for Data Inspection Strategies
# --------------------------------------------------
# This class defines a common interface for data inspection strategies.
# Subclasses must implement the inspect method.
class DataInspector(ABC):
    @abstractmethod
    def inspect_data(self, df: pd.DataFrame):
        """
        Perform a specific type of data inspection.

        Parameters:
        df (pd.DataFrame): The dataframe on which the inspection is to be performed.

        Returns:
        None: This method prints the inspection results directly.
        """
        pass

# Concrete Strategy for Data Types Inspection
# --------------------------------------------
# This strategy inspects the data types of each column and counts non-null values.
class BasicDataTypesInspection(DataInspector):
    def inspect_data(self, df: pd.DataFrame):
        """
        Inspects and prints the data types and non-null counts of the dataframe columns.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints the data types and non-null counts to the console.
        """
        print("\n--- Data Types Inspection ---")
        print(df.info())

# Concrete Strategy for Summary Statistics Inspection
# -----------------------------------------------------
# This strategy provides summary statistics for both numerical and categorical features.
class SummaryStatisticsInspection(DataInspector):
    def inspect_data(self, df: pd.DataFrame):
        """
        Prints summary statistics for numerical and categorical features.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints summary statistics to the console.
        """
        print("\n--- Summary Statistics(Numerical Feature) ---")
        print(df.describe())
        print("\n---- Summary Statistics(Categorical Feature) ---")
        print(df.describe(include=["object"]))

# Context Class that uses a DataInspectionStrategy
# ------------------------------------------------
# This class allows you to switch between different data inspection strategies.
class DataInspectionContext:
    def __init__(self, strategy: DataInspector):
        """
        Initializes the DataInspector with a specific inspection strategy.

        Parameters:
        strategy (DataInspectionStrategy): The strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspector):
        """
        Sets a new strategy for the DataInspector.

        Parameters:
        strategy (DataInspectionStrategy): The new strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        """
        Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Executes the strategy's inspection method.
        """
        self._strategy.inspect_data(df)

# Example Usage
# --------------
if __name__ == "__main__":
    pass
