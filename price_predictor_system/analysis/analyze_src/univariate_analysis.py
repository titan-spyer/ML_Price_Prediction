from abc import ABC, abstractmethod

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Abstract class for univariate analysis.
class UnivariateAnalysisTemplate(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature: str):
        pass


class NumericalAnalysis(UnivariateAnalysisTemplate):
    def analyze(self, df: pd.DataFrame, feature: str):
        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde=True, bins=30)
        plt.title(f"Distrubutin of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()

class CategoricalAnalysis(UnivariateAnalysisTemplate):
    def analyze(self, df: pd.DataFrame, feature: str):
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x=feature)
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

class UnivariateAnalyzer:
    def __init__(self, strategy: UnivariateAnalysisTemplate):
        """
        Initializes the UnivariateAnalysisContext with a specific analysis strategy.

        Parameters:
        strategy (UnivariateAnalysisTemplate): The strategy to be used for univariate analysis.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: UnivariateAnalysisTemplate):
        """
        Sets a new strategy for the UnivariateAnalysisContext.

        Parameters:
        strategy (UnivariateAnalysisTemplate): The new strategy to be used.
        """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature: str):
        """
        Executes the univariate analysis using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature (str): The column name to analyze.
        """
        self._strategy.analyze(df, feature)


if __name__ == "__main__":
    pass

