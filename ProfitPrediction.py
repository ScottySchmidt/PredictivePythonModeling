import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import data
df=pd.read_csv(r"co_profit.csv")

x=df.iloc[:, :-1].values
y=df.iloc[:,4].values

# Encoding categorical data:
from sklearn.preprocessing import LabelEncoder, OneNotEncoder
label_encoder_x = LabelEncoder()

#Removing one dummy and Splitting Dataset:
x[:, 3] = label_encoder_x.fit_transform(x[:,3])

onehotencoder_x= OneHotEncoder(categorical_features=[3])
x=onehotencoder_x.fit_transform(x).toarray()

#Removing one category to avoid dummy, variable trap:
x= x[:,1]

# Splitting dataset:
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =0.2, random_state=0)

#Fitting multiple linear regression models to training data:
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)
regressor.intercept_
regressor.coef_

# Predicting ttest set results:
pred = regressor.predict(x_test)

#RMSE: Mean squared error
from sklearn.metrics import mean_squared_error

rmse = sqrt(mean_squared_error(y_test, pred))

#Stats Model to Make Opitimal Model:
import statsmodels.api as sm
x = sm.add_constant(x)

import statsmodel.formula.api as smf
x_all=x[:, [0, 1, 2, 3, 4, 5]]

regressor_smf=smf.OLS(endog = y, exog =x_all).fit()
regressor_smf =smf.OLS(endog = y, exog = x_all).fit()
regressor_smf.summary()

#STEPS TO MAKE OPTIMAL:
x_all = x [: , [0, 1, 3, 4, 5]]
regressor_smf = =smf.OLS(endog = y, exog = x_all).fit()
regressor_smf.summary()

#Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =0.2, random_state=0)
regressor_2 = smf.OLS(endog = y_train, exog = x_train[:, [0:3]]).fit()

# Predictions:
pred2= regressor_2.predict(x_test[:. [0,3]])
rmse2 = sqrt(mean_squared_error(y_test, pred2))

'''
R2 shows how well data points for a curve or line.
Adjusted R2 also indicates how well terms fit a curve, but adjusts for the number of data points.
*If you add more useless variables to a model, adjusted R2 will decrease.
*If you add more useful variables to a model, adjusted R2 will increase.
Adjusted R2 will always be less than or equal to R2. You only need R2 when working with samples.
In other words, R2 is not neccessary when you have data from an entire population.
'''

#Final Model Implementation:
regressor3 = smf.OLS(endog = y_train, exog = x_train[: [0, 3, 5]])
rmse3 = sqrt(mean_squared_error(y_test, pred3)




