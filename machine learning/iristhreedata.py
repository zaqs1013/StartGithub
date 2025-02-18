import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
knn_train_acc = knn.score(X_train_scaled, y_train)
knn_test_acc = knn.score(X_test_scaled, y_test)
print("knn: ",knn_train_acc)
print(knn_test_acc)

lr = LogisticRegression(C = 1.0,max_iter=10)
lr.fit(X_train_scaled, y_train)
lr_train_acc = lr.score(X_train_scaled, y_train)
lr_test_acc = lr.score(X_test_scaled, y_test)
print("lr: ",lr_train_acc)
print(lr_test_acc)

dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)
dt_train_acc = dt.score(X_train, y_train)
dt_test_acc = dt.score(X_test, y_test)
print("dt: ",dt_train_acc)
print(dt_test_acc)
#plt.figure(figsize=(15,10))
#plot_tree(dt, filled=True, feature_names=feature_names)
#plt.show()

