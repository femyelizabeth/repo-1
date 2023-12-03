# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import tree

wine = pd.read_csv("WineQT.csv")
print(wine.head())
print(wine.info())
print(wine.describe())

x = wine.drop('quality', axis=1)
y = wine['quality']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

DT = DecisionTreeClassifier()
DT.fit(x_train, y_train)

y_pred = DT.predict(x_test)

print("(i) Classification Report:")
print(classification_report(y_test, y_pred))

print("(ii) Confussion Matrix:")
print(confusion_matrix(y_test, y_pred))

plt.figure(figsize=(15, 10))
tree.plot_tree(DT, feature_names=x.columns, class_names=[str(i) for i in DT.classes_], filled=True, rounded=True)
plt.show()
