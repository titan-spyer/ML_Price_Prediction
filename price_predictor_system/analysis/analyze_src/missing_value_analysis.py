from abc import ABC, abstractmethod

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Abstract Base class for missing Value analysis.
class MissingValueAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):
        self.missing_values_identification(df)
        self.visualize_missing_values(df)


    @abstractmethod
    def missing_values_identification(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def visualize_missing_values(self, df: pd.DataFrame):
        pass

# concrete  class for missing value analysis.
class SimpleMissingValueAnalysis(MissingValueAnalysisTemplate):
    def missing_values_identification(self, df: pd.DataFrame):
        print("\nMissing Values Count by Column:")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])

    def visualize_missing_values(self, df: pd.DataFrame):
        print("\nVisualizing Missing Values...")
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Values Heatmap")
        plt.show()

if __name__ == "__main__":
    pass