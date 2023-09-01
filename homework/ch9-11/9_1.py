import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.arange(1, 10, 1).reshape(3,3)
arr4 = np.zeros(3)


arr5 = arr2 + arr1
print(arr5)