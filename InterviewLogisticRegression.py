'''
LOGISTIC REGRESSION:
Step1: Clean and prepare your data: 
'''

import numpy as np
import pandas as pd
import time
import seaborn as sns

start=time.time()
print("Logistic regression analyst starting!")

df=r'C:\Users\scott\Desktop\exercise_40_train.csv' 
df=pd.read_csv(df)

#Drop columns that provide no numeric value:
df.drop(['x3', 'x7', 'x19',  'x24', 'x30', 'x31', 'x33', 'x39',
         'x42', 'x44', 'x49', 'x52', 'x57', 'x58', 'x60', 'x65', 
         'x67', 'x77', 'x93', 'x99'], axis = 1, inplace = True)

df.dropna(inplace=True) #delete any rows with missing values the simple way


'''
Step 2 - Build your models: 
For this exercise, you are required to build two models. The first model must be a logistic regression. 
The second model may be any supervised learning algorithm that is not from the GLM family.
'''

#LOGISTIC REGRESSION:
from sklearn.model_selection import train_test_split # splitting the data
from sklearn.linear_model import LogisticRegression # model algorithm
from sklearn import metrics
import matplotlib.pyplot as plt

y = np.asarray(df['y']) #This will ALWAYS stay the same as the depedent variable column.

#Split the data set into x and y data:
y_data = df['y']
x_data = df.drop('y', axis = 1)

#split the dataset into training (70%) and testing (30%) sets:
from sklearn.model_selection import train_test_split
x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x_data, y_data, test_size = 0.3, random_state=42)
#Logistic regression defaults to L2

#Create the model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

#Train the model and create predictions
model.fit(x_training_data, y_training_data)
predictions = model.predict(x_test_data)
#print(predictions)


'''
Step 3 - Generate predictions:
Create predictions on the data in test.csv using each of your trained models. 
The predictions should be the class probabilities for belonging to the positive class (labeled '1').  

Be sure to output a prediction for each of the rows in the test dataset (10K rows). 
Save the results of each of your models in a separate CSV file.  
Title the two files 'glmresults.csv' and 'nonglmresults.csv'. 
Each file should have a single column representing the predicted probabilities for its respective model. \
Please do not include a header label or index column. 
'''
results=[] #store results that will later be turned into a DF.

#Calculate performance metrics
from sklearn.metrics import classification_report
#print(classification_report(y_test_data, predictions))

#Generate a confusion matrix
from sklearn.metrics import confusion_matrix, roc_auc_score

#use model to predict probability that given y value is 1:
y_pred_proba = model.predict_proba(x_test_data)[::,1]

#calculate AUC of model
results=[]
auc = round( metrics.roc_auc_score(y_test_data, y_pred_proba), 4 ) 
print("AUC is: ", auc)
results.append(auc) #going to store results in a list


#acc = metrics.accuracy_score(y_test_data, predictions) #not needed
print(confusion_matrix(y_test_data, predictions))


# Create the pandas logistic regression pandas DataFrame:
#df=r'C:\Users\scot\Desktop\exercise_40_test' 
logDF = pd.DataFrame(results)
logDF.to_csv(r'C:\Users\Scott\Desktop\logDF.csv', index=False, header=False) #index, header = false gets rid of index, header  

print("Logistic regression program finished in: ",  round(time.time()-start, 3), " seconds.")

'''
Logistic regression analyst starting!
AUC is:  0.6216
[[33  4]
 [ 1  0]]
Logistic regression program finished in:  0.701  seconds.
'''
