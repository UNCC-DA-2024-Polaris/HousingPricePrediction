# IN PROGRESS

# Project 4 - Demystifying Machine Learning

**Date**: March 12, 2024

**Group**: Polaris

**Members**: David Bartlett, Kyndall Kelly, Rufin Perez, Kristina Swanson, Toby Wong

## Background
For the final group project, our group will use our machine learning skills gained in class to analyze, solve, or visualize a topic of our choice - i.e., predicting housing prices. Specifically, predicting housing prices on different features including area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hot water heating, air conditioning, parking, preferential area, and furnishing.

We began our process by creating a Python script to initialize, train, and evaluate regression models with our chosen dataset. Upon the initial model evaluations not meeting the 80% R-square requirement, we performed the following improvements:

* Created "dummy data" based on the existing features of the dataset
* Appended the dummy data records to the existing dataset and saved to a new csv file

We used that new csv file to re-run our existing Python script which resulted in achieving the 80% R-square requirement. However, our group decided to explore other models using the new csv file to determine if we could achieve and even better R-square score. We chose the following models:

* ADA Boost Classifier
* Decision Tree
* Random Forest Regressor
* Gradient Boosting Regressor

Based on each of the models' evaluation results, we determined the Decision Tree model to yield the highest result with 99.39%.

## Requirements

1. **Data and data delivery**

   * Obtained a housing prices dataset from Kaggle:
     - [Housing Price Prediction](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction): This dataset provides key features for predicting house prices - e.g., area, bedrooms, and bathrooms, and amenities - e.g., air conditioning, parking, and furnishing status information. It enables analysis and modelling to understand the factors impacting house prices and develop accurate predictions in real estate markets.


2. **Back end (ETL)**

   * Reviewed the dataset to ensure no missing fields and that it included consistent datatypes.
  
   * Preprocessed the categorical data in the DataFrame using "pd.get_dummies()" to convert the categorical variables into binary form for the model to perform better predictions
  
   * Preprocessed the numerical data in the DataFrame using the "StandardScaler()" to prepares the training and test datasets for the models by scaling the data to have a mean of zero and a standard deviation of one, which also improves model performance.
  
   * Created a table called, "HousingSQL", in SQL (PostgreSQL) using the Housing Price Prediction dataset.
  
   * Group members retrieved/extracted/exported the HousingSQL table from SQL to use with their respective models (during the exploratory phase of the project).
   
4. **Visualization**

   Based on our group's decision for choosing the Decision Tree model, we prepared a visualization of the resulting Decision Tree. However, due to the graphic being too large, we present two snippets of the full image for reference.

   ![DecisionTreeSnippet1](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/DecisionTreeSnippet1.png)

   ![DecisionTreeSnippet2](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/DecisionTreeSnippet2.png)

  
  **NOTE**: Please refer to ["DecisionTree Viz.png](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/DecisionTree%20Viz.png) for the full visualization of the Decision Tree. 
   

   

6. Group Presentation
  
7. Slide deck











_Data Model Implementation_ (25 points)
A Python script initializes, trains, and evaluates a model (10 points)

The data is cleaned, normalized, and standardized prior to modeling (5 points)

The model utilizes data retrieved from SQL or Spark (5 points)

The model demonstrates meaningful predictive power at least 75% classification accuracy or 0.80 R-squared. (5 points)

_Data Model Optimization_ (25 points)
The model optimization and evaluation process showing iterative changes made to the model and the resulting changes in model performance is documented in either a CSV/Excel table or in the Python script itself (15 points)

Overall model performance is printed or displayed at the end of the script (10 points)

_GitHub Documentation_ (25 points)
GitHub repository is free of unnecessary files and folders and has an appropriate .gitignore in use (10 points)

The README is customized as a polished presentation of the content of the project (15 points)

_Group Presentation_ (25 points)
All group members speak during the presentation. (5 points)

Content, transitions, and conclusions flow smoothly within any time restrictions. (5 points)

The content is relevant to the project. (10 points)

The presentation maintains audience interest. (5 points)
