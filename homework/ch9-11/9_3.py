'''
练习题：计算残差平方和

问题描述：
假设您有两组数据，分别是观测值和模型预测值。您需要编写一个函数，用于计算这两组数据之间的残差平方和，以衡量模型的拟合质量。

要求：

    创建一个函数 calculate_residual_sum_of_squares(observations, predictions)，该函数接受两个NumPy数组作为参数：
        observations：包含实际观测值的数组。
        predictions：包含模型预测值的数组。

    在函数中计算两组数据之间的残差数组，即每个观测值与对应的预测值之差。

    将残差数组的每个元素平方，然后求和，得到残差平方和。

    返回计算得到的残差平方和作为函数的输出。'''

import numpy as np

# 观测值和模型预测值
observations = np.array([15.0, 18.0, 22.0, 24.0, 28.0])
predictions = np.array([14.5, 17.8, 21.5, 23.8, 27.0])

# 定义计算残差平方和的函数
def calculate_residual_sum_of_squares(observations, predictions):
    pass

# 调用函数计算残差平方和
rss = calculate_residual_sum_of_squares(observations, predictions)
print("Residual Sum of Squares:", rss)


# def calculate_residual_sum_of_squares(observations, predictions):
#     residuals = observations - predictions
#     residuals_squared = residuals**2
#     rss = np.sum(residuals_squared)
#     return rss
