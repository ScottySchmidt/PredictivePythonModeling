'''
Python data science using KNN coding project.
Step1: Clean and prepare your data:
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

start=time.time()
print("Starting analyst for KNN classification:")

df=r'C:\Users\scott\Desktop\exercise_40_train.csv' 
df=pd.read_csv(df)

#Drop columns that provide no numeric value:
df.drop(['x3', 'x7', 'x19',  'x24', 'x30', 'x31', 'x33', 'x39',
         'x42', 'x44', 'x49', 'x52', 'x57', 'x58', 'x60', 'x65', 
         'x67', 'x77', 'x93', 'x99'], axis = 1, inplace = True)

df.dropna(inplace=True) #delete any rows with missing values the simple way.
#A more complex way would be to inmpute the mean for missing numeric values.

'''
Step 2 - Build your models: 
For this exercise, you are required to build two models. The first model must be a logistic regression. 
The second model may be any supervised learning algorithm that is not from the GLM family.
'''

# KNN using model2:
y = np.asarray(df['y']) #This will ALWAYS stay the same as the depedent variable column.

#Import standardization functions from scikit-learn
from sklearn.preprocessing import StandardScaler

#Standardize the data set
scaler = StandardScaler()
scaler.fit(df.drop('y', axis=1))
scaled_features = scaler.transform(df.drop('y', axis=1))
scaled_data = pd.DataFrame(scaled_features, columns = df.drop('y', axis=1).columns)

#Split the data set into training data and test data
from sklearn.model_selection import train_test_split
x = scaled_data
y = df['y'] #This will not change as the depedent variable
x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x, y, test_size = 0.3, random_state=42)
#Random state is needed or a different result will populate everytime.

'''
Step 3 - Generate predictions:
Create predictions on the data in test.csv using each of your trained models. 
The predictions should be the class probabilities for belonging to the positive class (labeled '1').  

Be sure to output a prediction for each of the rows in the test dataset (10K rows). 
Save the results of each of your models in a separate CSV file.  Title the two files 'glmresults.csv' and 'nonglmresults.csv'. 
Each file should have a single column representing the predicted probabilities for its respective model. \
Please do not include a header label or index column.
'''

'''
#Selecting an optimal K value:
error_rates = []
for i in np.arange(1, 40):
    new_model = KNeighborsClassifier(n_neighbors = i)
    new_model.fit(x_training_data, y_training_data)
    new_predictions = new_model.predict(x_test_data)
    error_rates.append(np.mean(new_predictions != y_test_data))

plt.figure(figsize=(16,12))
plt.plot(error_rates)

#Conclusion: The value this graph selected to use was 3 for n_neighbors.
'''
#Train the model and make predictions:
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors =3) #Must be an odd number to break a tie
model.fit(x_training_data, y_training_data)
predictions = model.predict(x_test_data)

#Performance measurement:
import sklearn.metrics as metrics
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
#print(classification_report(y_test_data, predictions))
#print(confusion_matrix(y_test_data, predictions))

#use model to predict probability that given y value is 1:
y_pred_proba = model.predict_proba(x_test_data)[::,1]

#calculate AUC of model
results=[] #store as a list to send to the csv file later on
auc = round( metrics.roc_auc_score(y_test_data, y_pred_proba), 4 ) 
print(auc)
results.append(auc) #going to store results in a list

#acc = metrics.accuracy_score(y_test_data, predictions) #not needed
print(confusion_matrix(y_test_data, predictions))


# Create the KNN predictive analytics pandas DataFrame:
df = pd.DataFrame(results)
df.to_csv(r'C:\Users\Scott\Desktop\nonglmresults.csv', index=False, header=False) #index, header=false gets rid of index, header 

print("Program Done! KNN data finished analyzing. ",  round(time.time()-start, 3), " seconds.")

'''
Starting analyst for KNN classification:
0.9595
[[34  3]
 [ 0  1]]
Program Done! KNN data finished analyzing.  0.654  seconds.


 precision    recall  f1-score   support

           0       0.92      0.94      0.93        35
           1       0.00      0.00      0.00         3

    accuracy                           0.87        38
   macro avg       0.46      0.47      0.46        38
weighted avg       0.84      0.87      0.86        38

[[33  2]
 [ 3  0]]
Program Done! KNN data finished analyzing.  0.828  seconds.
'''
