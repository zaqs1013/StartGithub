import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

temperature = np.array([15, 20, 25, 18, 22, 30, 12])
humidity = np.array([60, 70, 65, 75, 80, 50, 55])
growth = np.array([5.2, 6.1, 7.0, 5.5, 6.5, 8.0, 4.8])

input_data = np.column_stack((temperature, humidity))

plt.scatter(temperature, humidity) #그리는 부분
plt.xlabel("temperature")
plt.ylabel("humidity")
plt.show()

train_input, test_input, train_target, test_target = train_test_split(
    input_data, growth, test_size=0.2, random_state=50
)

knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(train_input, train_target)

predicted = knn.predict(test_input)
print(predicted)
print(test_target)

data = np.array([[20, 80]])
prediction = knn.predict(data)
print(prediction)