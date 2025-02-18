from sklearn.model_selection import train_test_split #훈련과 테스트를 분할한다.

X = iris.data
y = iris.tartget

#80,20으로 나눠서 훈련함. [총 150개의 데이터]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=4)

#random_state는 초기값을 주는거다.

print(X_train.shape) 
print(X_test.shape)