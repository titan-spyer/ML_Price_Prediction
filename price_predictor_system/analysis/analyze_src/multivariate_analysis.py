from abc import ABC, abstractmethod

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Abstract class for multivariate analysis
class MultivariateAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):
        """
        Perform a comprehensive multivariate analysis by generating a correlation heatmap and pair plot.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed.
        feature1 (str): The name of the first feature/column to be analyzed.
        feature2 (str): The name of the second feature/column to be analyzed.

        Returns:
        None: This method orchestrates the multivariate analysis process.
        """
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)

    @abstractmethod
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        """
        Generate and display a correlation heatmap for the numerical features in the dataframe.

        Parameters:
        df (pd.Dataframe): The dataframe containing the data to be analyzed.
        feature1 (str): The name of the first feature/column to be analyzed.
        feature2 (str): The name of the second feature/column to be analyzed.

        Returns:
        None: Displays a heatmap showing correlations between numerical features.
        """
        pass
    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame):
        """
        Generate and display a pair plot of the selected features.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed.
        feature1 (str): The name of the first feature/column to be analyzed.
        feature2 (str): The name of the second feature/column to be analyzed.

        Returns:
        None: Displays a pair plot for the selected features.
        """
        pass


class SimpleMultivariateAnalysis(MultivariateAnalysisTemplate):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        """
        Generate & display co relation heatmap for the numerical features in the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed.

        Returns:
        Display a correlation heatmap showing correlations between numerical features.
        """
        plt.figure(figsize=(12, 10))
        sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()

    def generate_pairplot(self, df: pd.DataFrame):
        """
        Generate & display pair plot for the selected features in the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed.

        Returns:
        Display a pair plot for the selected features.
        """
        sns.pairplot(df)
        plt.suptitle("Pair Plot of Selected Features", y=1.02)
        plt.show()


if __name__ == "__main__":
    pass