# Project 4 - Demystifying Machine Learning

**Date**: March 12, 2024

**Group**: Polaris

**Members**: David Bartlett, Kyndall Kelly, Rufin Perez, Kristina Swanson, Toby Wong

## Background
For the final group project, our group will use our machine learning skills gained in class to analyze, solve, or visualize a topic of our choice - i.e., predicting housing prices. Specifically, predicting housing prices on different features including area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hot water heating, air conditioning, parking, preferential area, and furnishing.

We began our process by creating a Python script to initialize, train, and evaluate regression models with our chosen dataset. Upon the initial model evaluations not meeting the 80% R-square requirement, we performed the following improvements:

* Created "dummy data" based on the existing features of the dataset
* Appended those dummy data records to the existing dataset and saved to a new csv file

We used that newly appended dataset (i.e., new csv file) to re-run in our existing Python script which resulted in achieving the 80% R-square requirement. However, our group decided to select several other models using the appended dataset to determine if we could find a better R-square score. We chose the following models:

* ADA Boost Classifier
* Decision Tree
* Random Forest Regressor
* Gradient Boosting Regressor

Based on each of the models' evaluation results, we determined the Decision Tree model to yield the highest result with 99.39%.


## Requirements

1. Data and data delivery

   * Obtained a housing prices dataset from Kaggle:
     - [Housing Price Prediction](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction): This dataset provides key features for predicting house prices - e.g., area, bedrooms, and bathrooms, and amenities - e.g., air conditioning, parking, and furnishing status information. It enables analysis and modelling to understand the factors impacting house prices and develop accurate predictions in real estate markets.


3. Back end (ETL)

   * We reviewed the dataset to ensure no missing fields and includes consistent datatypes.
  
   * Created a table called, "HousingSQL", in SQL (PostgreSQL) using the Housing Price Prediction dataset.
  
   * Group members retrieved/extracted the HousingSQL table from SQL to use with their respective models.
  
   * Group membe
   
4. Visualizations

5. Group Presentation
  
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
