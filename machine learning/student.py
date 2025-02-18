# 로지스틱 회귀 모델: 시험 합격 여부 예측 이진 분류에 포함됨.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

#1부터 100까지 데이터를 50개 생성함.
student_scores = np.random.randint(1, 101, 50)
print("학생 점수:", student_scores)

#astype 메서드는 열의 요소의 데이터 타입을 변경하는함수
pass_score = (student_scores >= 70).astype(int) 
print("합격 여부 (0=불합격, 1=합격):", pass_score)

#1차원 배열을 2차원 데이터로 변환(10행,1열로 변환)
X = student_scores.reshape(-1, 1) 
y = pass_score

#데이터 스케일링 80%훈련 20% 테스트
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)

#StandardScaler()는 표준화
scaler = StandardScaler() 

#fit는 데이터를 학습하여 스케일링 기준(평균, 표준편차 등)을 저장
#transform는 학습과 변환을 수행함.
X_train_scaled = scaler.fit_transform(X_train)  
X_test_scaled = scaler.transform(X_test)

#로지스틱회귀 모델 적용, C는 규제를 의미함.
lr = LogisticRegression(C=0.1) #로지스틱 회귀 모델
lr.fit(X_train_scaled, y_train)
#fit 함수는 반드시 2차원 배열을 요구

train_accuracy = lr.score(X_train_scaled, y_train)
test_accuracy = lr.score(X_test_scaled, y_test)
print("훈련 데이터 정확도:", train_accuracy)
print("테스트 데이터 정확도:", test_accuracy)

# 새로운 점수 예측
new_score = np.array([[70]])  # 학생 점수
new_score_scaled = scaler.transform(new_score)  # 표준화 적용
prediction = lr.predict(new_score_scaled)  # 합격 여부 예측
probability = lr.predict_proba(new_score_scaled)[:, 1]  # 합격 확률

print(f"새로운 점수 {new_score[0][0]}의 예측 결과: {'합격' if prediction[0] == 1 else '불합격'}")
print(f"합격 확률: {probability[0]:.2f}")
