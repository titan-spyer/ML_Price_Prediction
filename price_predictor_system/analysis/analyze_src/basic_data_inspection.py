from abc import ABC, abstractmethod

import pandas as pd


# Context Basic Data Inspection
class DataInspector(ABC):
    @abstractmethod
    def inspect_data(self, df: pd.DataFrame):
        '''
        Abstract method to inspect data.

        parameter: take  the data to be inspected.

        return: None
        '''
        pass


class BasicDataTypesInspection(DataInspector):
    def inspect_data(self, df: pd.DataFrame):
        '''
        Inspect data types of the columns in the dataframe.

        parameter: data (pd.DataFrame)
        return: None
        '''
        print("\n--- Data Types Inspection ---")
        print(df.info())


class SummaryStatisticsInspection(DataInspector):
    def inspect_data(self, df: pd.DataFrame):
        '''
        Inspect summary statistics of the dataframe.

        parameter: data (pd.DataFrame)
        return: None
        '''
        print("\n--- Summary Statistics(Numerical Feature) ---")
        print(df.describe())
        print("\n---- Summary Statistics(Categorical Feature) ---")
        print(df.describe(include=["0"]))


class DataInspectionContext:
    def __init__(self, strategy: DataInspector):
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspector):
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        self._strategy.inspect_data(df)
