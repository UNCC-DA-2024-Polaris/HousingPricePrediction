# Project 4 - Demystifying Machine Learning

**Date**: March 12, 2024

**Group**: Polaris

**Members**: David Bartlett, Kyndall Kelly, Rufin Perez, Kristina Swanson, Toby Wong

## Background
For the final group project, our group will use our machine learning skills gained in class to analyze, solve, or visualize a topic of our choice - i.e., predicting housing prices. Specifically, predicting housing prices on different features including area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hot water heating, air conditioning, parking, preferential area, and furnishing.

We began our process by creating a Python script to initialize, train, and evaluate regression models with our chosen dataset ([Housing.csv](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/resources/Housing.csv). Upon the initial model evaluations not meeting the 80% R-square requirement, we performed the following improvements:

* Created "dummy data" based on the existing features of the dataset.
* Appended the dummy data records to the existing dataset and saved to a new csv file ([HousingSQL.csv](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/resources/HousingSQL.csv).

We used that new csv file to re-run our existing Python script which resulted in achieving the 80% R-square requirement. However, our group decided to explore other models using the new csv file to determine if we could achieve and even better R-square score. We chose the following models:

* Ridge Regression
* Lasso Regression
* Linear Regression
* Elastic Net Regression
* Ada Boost Classifier
* Gradient Boost Regressor
* Random Forest Regression
* Decision Tree Regression

Based on each of the models' evaluation results, we determined the Decision Tree Regression model to yield the highest result with an R-square of 92.49%.

## Requirements

1. **Data and data delivery**

   * Obtained a housing prices dataset from Kaggle:
     - [Housing Price Prediction](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction): This dataset provides key features for predicting house prices - e.g., area, bedrooms, and bathrooms, and amenities - e.g., air conditioning, parking, and furnishing status information. It enables analysis and modelling to understand the factors impacting house prices and develop accurate predictions in real estate markets.
  
   * Used Python scripts documented in ["main.ipynb"](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/main.ipynb) and ["HousingPriceProjectModel_DecisionTree.ipynb"](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/HousingPriceProjectModel_DecisionTree.ipynb) notebooks to initialize, train, and evaluate our models.

2. **Back end (ETL)**

   * Reviewed and cleaned the dataset to ensure no missing fields and that it included consistent datatypes.
  
   * Preprocessed the categorical data in the DataFrame using "pd.get_dummies()" to convert the categorical variables into binary form for the model to perform better predictions
  
   * Preprocessed the numerical data in the DataFrame using the "StandardScaler()" to prepares the training and test datasets for the models by scaling the data to have a mean of zero and a standard deviation of one, which also improves model performance.
  
   * We used “dummyData.py” to generate additional rows based on the existing parameters of the original dataset, to keep the data proportioned and varied, including reducing the impact of outliers. We then concatenated the original ‘df’ and ‘dummy_df’ which increased the dataset from 545 rows to 80,545 rows.
  
   * Created a table called, "HousingSQL", in SQL (PostgreSQL) using the [Housing Price Prediction](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction) dataset.
  
   * Group members retrieved/extracted/exported the HousingSQL table from SQL to use with their respective models (during the exploratory phase of the project).
   
3. **Visualization**

   Based on our group's decision for choosing the Decision Tree model, we prepared a visualization of the resulting Decision Tree. However, due to the graphic being too large, we present the following two snippets of the full image for reference.

   ![DecisionTreeSnippet1](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/Images/DecisionTreeSnippet1.png)

   ![DecisionTreeSnippet2](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/Images/DecisionTreeSnippet2.png)

   **NOTE**: Please refer to ["DecisionTree Viz.png"](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/Images/DecisionTree%20Viz.png) for the full visualization of the Decision Tree.
   
4. Group Presentation and 5. Slide Deck
   Our group presented our model results during class presentation on 3/12/24. Please refer to our presentation slide deck at: [Project 4 - Polaris.pdf](https://github.com/UNCC-DA-2024-Polaris/HousingPricePrediction/blob/main/Project%204%20-%20Polaris.pdf).  

## Sources and References

* Housing Price Prediction by Harish Kumardatalab
[https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction)

* [https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

* [https://deepai.org/machine-learning-glossary-and-terms/dummy-variable#:~:text=Dummy%20variables%20are%20binary%20](https://deepai.org/machine-learning-glossary-and-terms/dummy-variable#:~:text=Dummy%20variables%20are%20binary%20)
