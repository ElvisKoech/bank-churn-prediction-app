# bank-churn-prediction-data-app
# Required Files
setup.sh
procfile
requirement.txt
+ App: 
[Bank Churn Prediction Data App](https://elviskoech-bank-churn-prediction-app-main-y0c4q1.streamlit.app/)

## Project Outline
+ Problem Statement
+ Dataset Information
+ Feature Processing and Feature Engineering
+ Machine Learning Model Development
+ Evaluating the result/metrics
+ Conclusion

## Problem Statement
+ Customer retention is one of the primary growth pillars for products with a subscription-based business model. Several bad experiences – or even one – and a customer may quit. And if droves of unsatisfied customers churn at a clip, both material losses and damage to reputation would be enormous.
+ Customer churn (or customer attrition) is a tendency of customers to abandon a brand and stop being a paying client of a particular business.
+ I used supervised machine learning classification approach to solve this problem and based on the number of target class I built a binary classifier type of ML model.

## Dataset Information
+ Data Source : Github 
+ Columns : 14
+ Rows    : 10000

## Feature Processing and Feature Engineering
+ I used SelectKBest and ExtraTreesClassifier from Sklearn library to find the best features

## Machine Learning Model Development
+ Using LogisticRegression ML Estimator our model had an accuracy score of 0.813(81.3%)
+ I had to evaluate the model further using Classification report and Cross validation 

## Evaluating the result/metrics
+ Cross Validation had an accuracy of 80.73%
+ Comparing the logistic Regression model to:
   + Decision Tree Classifier
   + Random Forest Classifier
   + Support Vector Machine
   + K nearest Classifier
   + naive_bayes
+ Using Classification Report to determine F1_Score of different models:
   + LR F1-score 0.5958600508740877
   + DT F1-score 0.6895821798155766
   + RF F1-score 0.7513784461152883
   + SVM F1-score 0.5210022107590273
   + NB F1-score 0.6412824619876383
   + KNN F1-score 0.6245016923566131
+ Random Forest Classifier model performed well compared to other models
+ To improve the accuracy of the Random Forest model I used RandomSearchCv to tune the hyperparameters:
   + Hence the randomised search cv on random forest classifier gave us better accuracy which is 86.25% and a std of 0.99% and wrong predictions made by the model are 374/2000

## Conclusion
+ To conclude, we can use these ML models to predict customer churn with a higher accuracy and metrics
+ In general, it’s the overall customer experience that defines brand perception and influences how customers recognize value for money of products or services they use.
+ The reality is that even loyal customers won’t tolerate a brand if they’ve had one or several issues with it.




