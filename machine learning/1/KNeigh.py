from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)

print(y_pred)
print(y_test)

score =  metrics.accuracy_score(y_test,y_pred)
print(score)