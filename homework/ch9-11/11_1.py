from matplotlib import pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])
z = x ** 2

plt.plot(x, z)
plt.xlabel('X 轴')
plt.ylabel('Y 轴')
plt.title('y-x')
plt.show()