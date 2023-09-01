import numpy as np

a = np.array([1, 2, 3, 4]).reshape(2, 2)
b = np.array([4, 5, 6, 7]).reshape(2, 2)

c = a + b
d = a * 2
e = a * b


print(c)
print(d)
print(e)