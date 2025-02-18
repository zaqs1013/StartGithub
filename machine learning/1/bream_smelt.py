import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


# 물고기 데이터 (길이, 무게)
fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]

fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 데이터를 numpy 배열로 변환
input_arr = np.array([[l, w] for l, w in zip(fish_length, fish_weight)])
target_arr = np.array([1] * 35 + [0] * 14)

# k-최근접 이웃 모델 생성
kn = KNeighborsClassifier(n_neighbors=5)
kn.fit(input_arr, target_arr)

# 모델 평가
print("모델 정확도:", kn.score(input_arr, target_arr))

# 새로운 데이터 예측
new_data = [[30, 600]]
prediction = kn.predict(new_data)
print(f"길이 30cm, 무게 600g의 예측 결과: {prediction}")

# 과적합 테스트 (k=49)
kn49 = KNeighborsClassifier(n_neighbors=49)
kn49.fit(input_arr, target_arr)
print("k=49 모델 정확도:", kn49.score(input_arr, target_arr))

# 1의 비율 출력
print(f"데이터에서 1의 비율: {35/49:.2f}")

# 무작위 데이터 셔플링 (seed 고정)
np.random.seed(42)
index = np.arange(49)
np.random.shuffle(index)

# 훈련 데이터 및 타겟 설정
train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

print("훈련 데이터 샘플:", train_input[:5])  # 일부만 출력해서 확인
print("훈련 타겟 샘플:", train_target[:5])  # 일부만 출력해서 확인

pit.scatter(train_input[:,0], train_input[:,1])
it.scatter(test_input[:,0],test_input[:,1])

kn = kn.fit(train_input, train_target)
kn.score(test_input, test_target)