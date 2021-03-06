'''
LINEAR REGRESSION:
I thought linear regression might provide a better AUC than 0.62 which was the logistic regression.

Step1: Clean and prepare your data:
The data in this exercise have been simulated to mimic real, dirty data. 
Please clean the data with whatever method(s) you believe to be best/most suitable. 
Success in this exercise typically involves feature engineering and avoiding data leakage. 
You may create new features. However, you may not add or supplement with external data. 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import time

'''
Step1: Clean and prepare your data: 
'''

start=time.time()
print("Linear regression classification starting!")

df=r'C:\Users\scott\Desktop\exercise_40_train.csv' 
df=pd.read_csv(df)

#Drop columns that provide no numeric value:
df.drop(['x3', 'x7', 'x19',  'x24', 'x30', 'x31', 'x33', 'x39',
         'x42', 'x44', 'x49', 'x52', 'x57', 'x58', 'x60', 'x65', 
         'x67', 'x77', 'x93', 'x99'], axis = 1, inplace = True)

df.dropna(inplace=True) #delete any rows with missing values the simple way.
#A more complex way would be to inmpute the mean for 

'''
Step 2 - Build your models: 
For this exercise, you are required to build two models. The first model must be a logistic regression. 
The second model may be any supervised learning algorithm that is not from the GLM family.
'''

#Split the data set into x and y data
y_data = df['y']
#print(y_data)
x_data = df.drop('y', axis = 1)

#Split the data set into training data and test data
from sklearn.model_selection import train_test_split
x_train_data, x_test_data, y_train_data, y_test_data = train_test_split(x_data, y_data, test_size = 0.3, random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train_data, y_train_data)
print(model.coef_)
#print(model.intercept_)

'''
Step 3 - Generate predictions:
Create predictions on the data in test.csv using each of your trained models. 
The predictions should be the class probabilities for belonging to the positive class (labeled '1').  
'''

pd.DataFrame(model.coef_, x_data.columns, columns = ['Coeff'])
predictions = model.predict(x_test_data)
#print( round(predictions, 4)  )

# plt.scatter(y_test, predictions)
plt.hist(y_test_data - predictions)

#Performance measurement:
import sklearn.metrics as metrics
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
#print(classification_report(y_test_data, predictions))
#print(confusion_matrix(y_test_data, predictions))

metrics.mean_absolute_error(y_test_data, predictions)
metrics.mean_squared_error(y_test_data, predictions)
np.sqrt(metrics.mean_squared_error(y_test_data, predictions))


#use model to predict probability that given y value is 1:
y_pred_proba = model.predict(x_test_data)

#calculate AUC of model
results=[]
auc = round( metrics.roc_auc_score(y_test_data, y_pred_proba), 4 ) 
print("AUC is: ", auc)
results.append(auc) #going to store results in a list


# Create the KNN predictive analytics pandas DataFrame:
df = pd.DataFrame(results)
df.to_csv(r'C:\Users\Scott\Desktop\linear.csv', index=False, header=False) #index, header=false gets rid of index, header 
print("Linear regression program finished in: ",  round(time.time()-start, 3), " seconds.")

'''
Linear regression classification starting!
[-9.65155966e-04  9.43735413e-01  8.01621971e-03  5.14224733e-01
  2.12441510e-01  1.42490885e-01  1.96371912e-01 -6.38759802e-01
  1.13408472e-01 -2.87772937e-01  1.35667343e-01 -2.17965963e-01
  2.75248930e-01  5.22348418e-01 -1.24801633e-01  4.91592462e-03
 -1.76273716e-01  3.15862262e-03 -4.17862264e-03 -1.42521918e-01
 -5.23258738e-03 -2.29934146e-02  9.25142983e-03  4.39673212e-02
  1.68544784e-03  2.24350962e-02  1.52488588e-01 -8.25921486e-02
  1.47751584e-01  2.74998507e-01  2.24607167e-03  2.36554438e-01
 -5.77662495e-04 -2.40727660e-02 -9.06863825e-02  2.06365340e-01
 -4.44023667e-01  3.33867224e-02 -6.64550263e-04  2.36245052e-02
  4.83317058e-02 -2.12937653e-02 -1.50220748e-01 -4.33274899e-02
  2.11840659e-01  5.72680521e-02 -4.19147685e-03 -1.41141674e-01
 -1.27986599e-01 -1.98925876e-01  8.56492892e-02  2.83879661e-02
  6.39138388e-01 -7.17555268e-02  1.23839815e-01  7.44883030e-02
  1.38009659e-01  1.55854871e-01 -5.01285806e-02  3.59430533e-01
  5.07895349e-01 -2.16858063e-01  6.88642811e-02 -3.09738539e-02
 -6.50023092e-02  3.34505136e-02  3.21371844e-02 -1.83571526e-01
 -9.28423756e-02  2.53434566e-01 -3.90854546e-02  9.41805684e-01
  1.85360926e-01 -7.36703950e-02  3.66492790e-01  1.54611619e-01
  7.28291116e-02  1.92544471e-03  6.69967864e-03 -4.83199747e-02]
AUC is:  0.9189
Linear regression program finished in:  1.511  seconds.
'''
