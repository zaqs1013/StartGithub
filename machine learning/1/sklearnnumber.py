import matplotlib.pyplot as plt #숫자 이미지 파일
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
digits = datasets.load_digits()
plt.imshow(digits.images[0], cmap=plt.cm.gray_r,interpolation='nearest')