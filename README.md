# End-to-End Machine Learning Architecture: Price Predictor System

## 📌 Project Overview
This repository is a structured, production-ready Machine Learning pipeline designed to predict housing prices. Rather than building the model in a single, monolithic Jupyter Notebook, this project was developed to master **Machine Learning System Architecture** and **Clean Code Principles**. 

The focus of this project is on modularity, robust data handling, and applying software engineering design patterns to the ML lifecycle.

## 🧠 Key Learnings & Architecture Highlights
Building this system provided hands-on experience with deploying a scalable ML architecture. Key takeaways include:

* **Modular Pipeline Design:** Breaking down the monolithic ML process into independent, reusable, and testable steps (Ingestion, Processing, Training).
* **Software Design Patterns in ML:**
  * **Factory Pattern:** Implemented in Data Ingestion to dynamically handle different file types (e.g., `.zip`, `.csv`).
  * **Strategy Pattern:** Used in Outlier Detection and Missing Value Handling to easily switch between different mathematical approaches (e.g., Z-score vs. IQR, Mean imputation vs. Dropping) without rewriting core logic.
  * **Template Pattern:** Applied in the exploratory data analysis structure to enforce a consistent sequence of analytical steps.
* **Experiment Tracking:** Integrating `MLflow` to automatically log model parameters, metrics, and artifacts during the training phase.

## 🔄 The Data Handling Lifecycle
This pipeline rigorously follows the standard data science lifecycle, with dedicated modules for each phase:

1. **Data Ingestion:** Securely extracting and loading raw data from compressed sources.
2. **Data Inspection & EDA:**
   * **Missing Value Analysis:** Identifying the scope of incomplete data.
   * **Univariate Analysis:** Examining the distribution of individual features.
   * **Bivariate Analysis:** Exploring relationships between specific features and the target variable.
   * **Multivariate Analysis:** Understanding complex feature interactions and correlations.
3. **Data Preprocessing:**
   * **Missing Value Handling:** Applying statistical strategies to fill or drop gaps.
   * **Feature Engineering:** Transforming distributions (e.g., Log transformations on skewed data).
   * **Outlier Detection:** Mathematically isolating and mitigating extreme anomalies.
4. **Data Splitting:** Safely partitioning data to prevent data leakage.
5. **Model Building & Pipeline Integration:** Wrapping Scikit-Learn preprocessing (Imputation, One-Hot Encoding) and the Linear Regression model into a single, cohesive pipeline for training.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn
* **Tracking & Orchestration:** MLflow
* **Environment:** Google Colab

## 🚀 Execution Flow
The main execution of the pipeline is orchestrated via the `training_pipeline.py` script, which sequentially triggers the steps from data ingestion through to the final trained model pipeline.