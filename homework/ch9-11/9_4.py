'''
练习题：数据正则化

问题描述：
您需要编写一个函数，该函数接受一个包含数值数据的NumPy数组，并返回正则化后的数组。正则化是一种常见的数据预处理技术，用于将不同尺度和范围的数据映射到相同的尺度，通常在[0, 1]范围内。

要求：

    创建一个函数 normalize_data(data)，该函数接受一个NumPy数组 data 作为参数。

    在函数中，计算数据的均值与标准差。

    使用以下公式将数据正则化到[0, 1]范围内的新值：
    x = (x - x_mean) / x_std
    
    
    返回包含正则化后的数据的NumPy数组。
'''

import numpy as np

# 原始数据
data = np.array([10.0, 20.0, 30.0, 40.0, 50.0])

# 定义数据正则化函数
def normalize_data(data):
    pass

# 调用函数进行数据正则化
normalized_data = normalize_data(data)
print("Normalized Data:", normalized_data)


# def normalize_data(data):
#     data_mean = data.mean()
#     data_std = np.std(data)
#     normalized_data = (data - data_mean) / data_std
#     return normalized_data