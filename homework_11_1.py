import requests
import numpy as np
import matplotlib.pyplot as plt

url = 'https://httpbin.org/get'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Failed to fetch data')




# Создание массива чисел
arr = np.array([1, 2, 3, 4, 5])

# Сложение всех элементов массива
sum_result = np.sum(arr)

# Умножение всех элементов массива
prod_result = np.prod(arr)

print("Сумма элементов массива:", sum_result)
print("Произведение элементов массива:", prod_result)



x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()
