'''
Random Forest classification predictive model.
The first column 'y' is the independent variable being analyzed for this project.
'''

#Numerical computing libraries
import pandas as pd
import numpy as np
import time

#Visalization libraries
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#Import the data set
df=r'C:\Users\scott\Desktop\exercise_40_train.csv' 
df=pd.read_csv(df)

start=time.time()
print("Starting random forest classification analysis.")

''' STEP1: CLEAN THE DATA '''

#Drop columns that provide no numberic value:
df.drop(['x3', 'x7', 'x19',  'x24', 'x30', 'x31', 'x33', 'x39',
         'x42', 'x44', 'x49', 'x52', 'x57', 'x58', 'x60', 'x65', 
         'x67', 'x77', 'x93', 'x99'], axis = 1, inplace = True)

df.dropna(inplace=True) #delete any rows with missing values the simple way.

''' STEP2: TRAIN THE DATA '''

#Split the data set into training data and test data
from sklearn.model_selection import train_test_split
x = df.drop('y', axis = 1)
y = df['y']
x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x, y, test_size = 0.3, random_state=42)

#Train the decision tree model
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_training_data, y_training_data)
predictions = model.predict(x_test_data)

''' STEP3: PREDICT THE DATA '''

#Measure the performance of the decision tree model
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, r2_score
print(classification_report(y_test_data, predictions))
print(confusion_matrix(y_test_data, predictions))

#Train the random forests model
from sklearn.ensemble import RandomForestClassifier
random_forest_model = RandomForestClassifier()
random_forest_model.fit(x_training_data, y_training_data)
random_forest_predictions = random_forest_model.predict(x_test_data)

'''
STEP 3: MAKE PREDICTIONS:
'''

#Make predictions with the model
predictions = model.predict(x_test_data)

#Performance measurement:
import sklearn.metrics as metrics
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
#print(classification_report(y_test_data, predictions))
#print(confusion_matrix(y_test_data, predictions))

metrics.mean_absolute_error(y_test_data, predictions)
metrics.mean_squared_error(y_test_data, predictions)
np.sqrt(metrics.mean_squared_error(y_test_data, predictions))


print(classification_report(y_test_data, predictions))
print(confusion_matrix(y_test_data, predictions))

#use model to predict probability that given y value is 1:
y_pred_proba = model.predict(x_test_data)

#calculate AUC of model
results=[]
auc = round( metrics.roc_auc_score(y_test_data, y_pred_proba), 4 ) 
print("AUC is: ", auc)
results.append(auc) #going to store results in a list

tree = pd.DataFrame(results)
tree.to_csv(r'C:\Users\Scott\Desktop\tree.csv', index=False, header=False) #index, header = false gets rid of index, header  
print("Random forest classification analysis program finished in: ",  round(time.time()-start, 3), " seconds.")


'''
Starting random forest classification analysis.
              precision    recall  f1-score   support

           0       0.97      0.84      0.90        37
           1       0.00      0.00      0.00         1

    accuracy                           0.82        38
   macro avg       0.48      0.42      0.45        38
weighted avg       0.94      0.82      0.87        38

[[31  6]
 [ 1  0]]
              precision    recall  f1-score   support

           0       0.97      0.84      0.90        37
           1       0.00      0.00      0.00         1

    accuracy                           0.82        38
   macro avg       0.48      0.42      0.45        38
weighted avg       0.94      0.82      0.87        38

[[31  6]
 [ 1  0]]
AUC is:  0.4189
Random forest classification analysis program finished in:  1.34  seconds.
'''
