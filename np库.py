import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(arr))

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr * arr1)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
arr1 = arr.reshape(4, 2)
print(arr1)
arr_T = arr.transpose()
print(arr_T)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
a = np.dot(arr1, arr2)
print(a)
print(arr1.mean())
print(arr1.max())
print(arr1.min())
print(arr1.std())
print(np.sort(arr1))
print(np.sort(arr.reshape(-1)))
print(arr > 5)
print(arr[arr > 5])
print(arr[(arr > 3) & (arr < 6)])

np.random.seed(1)
print(np.random.rand())
arr = np.random.randint(0, 100, 16).reshape(4, 4)
print(arr[arr <= 10])
