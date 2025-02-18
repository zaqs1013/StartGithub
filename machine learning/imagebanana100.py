import numpy as np
import matplotlib.pyplot as plt

fruits = np.load('fruits_300.npy')

banana = fruits[200:300].reshape(-1, 100*100)  # 바나나 데이터만 선택
banana_mean = np.mean(banana, axis=0).reshape(100, 100)  # 바나나 평균 이미지 생성

abs_diff = np.abs(fruits[200:300] - banana_mean)  # 바나나와의 차이 계산
abs_mean = np.mean(abs_diff, axis=(1, 2))  # 각 이미지별 차이 평균 계산

banana_index = np.argsort(abs_mean) + 200  # 바나나 100개 중 가장 비슷한 순서로 정렬

fig, axs = plt.subplots(10, 10, figsize=(10, 10))
axs = axs.flatten()

for i in range(100):
    axs[i].imshow(fruits[banana_index[i]], cmap='gray_r')
    axs[i].axis('off')

plt.show()
