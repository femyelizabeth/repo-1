# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.model_selection import train_test_split
'''
salary = pd.read_csv("Salary_Data.csv")
print(salary.info())
print(salary.head())
print(salary.describe())

print(salary.isnull().sum())

datamap = sns.heatmap(salary.corr(), annot=True)
plt.show()

x = np.array(salary['YearsExperience']).reshape(-1, 1)
y = np.array(salary['Salary']).reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, test_size=0.3, random_state=100)

regr = LinearRegression()
regr.fit(x_train, y_train)

y_pred = regr.predict(x_test)
print("predicted salary")
for i in range(len(y_test)):
    print('%2f %2f' %(y_test[i], y_pred[i]))'''

age = np.array([18, 22, 30, 45, 65, 80]).reshape(-1, 1)
accdnt_no = np.array([38, 36, 24, 20, 18, 28]).reshape(-1, 1)

regr = LinearRegression()
regr.fit(age, accdnt_no)

accdnt_pred = regr.predict(age)

plt.scatter(age, accdnt_no, label='Points')
plt.plot(age, accdnt_pred, label='Linear Regression')
plt.legend()
plt.show()

pred1 = regr.predict([[40]])
pred2 = regr.predict([[60]])

print(f'Accidents for age 40 is:{pred1[0]}')
print(f'Accidents for age 60 is:{pred2[0]}')
