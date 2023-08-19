### This is Repository for Technical Test Data Scientist - AgriAku

*1. Before you build any model, you want first to explore the raw data. What kind of analyses you would do? What kind of data pre-processing you would do? Please explain your logic and show the result of your preparatory analyses. [Point 7]*

*Anwer :
Analysis :
1. Statistic Summary for the numerical features
2. Categorical feature analysis
3. Histogram
4. Correlation ALaysis

Data Preprocessing:
1. Handling Outliers
2. Feature Scaling and Encoding*

*2.Can you build a Machine Learning model (not Artificial Neural Network) to categorize the alcohol molecule given readings from the electronic nose? (Please consider the MIP: NP ratio as one of the features as well) Please justify your choice of algorithm and walk us through your logic as you develop the model. What is the accuracy, precision, and recall of the model? [Point 10]*

*Answer:
for the Machine Learning Model, I used 5 Algorithm ( Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors, and AdaBoost. after training using baseline model we found that **Decision Tree Model** have the best result with accuracy for Train Data (0.8398) and Test Data (0.8684). to improve the model we use Hyperparameter tuning and the result is accuracy for Train Data (0.8509) and Test Data (0.8684).*

*Table below is the classfication report from our model*
|  |Train  |Test	|
|--|--|--|
| Accuracy |  |	|
| Precision|  |	|
| Recall|  |	| |

*3.Can you build an Artificial Neural Network (ANN) model to categorize the alcohol molecule given readings from the electronic nose? (Please consider the MIP:NP ratio as one of the features as well) Please justify your choice of algorithm and walk us through your logic as you develop the model. What is the accuracy, precision, and recall of the model? [Point 10]*

  

*4.You were asked to convert your model to API, so that the researchers can perform the alcohol identification in real-time. How would you do this (you don’t have to make the actual API)? [Point 8]*
