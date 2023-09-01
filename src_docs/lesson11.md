#  数据可视化常用库: matplotlib

## 1. 什么是 Matplotlib？

Matplotlib 是 Python 的一个绘图库，用于创建静态、交互式和动态图表。它提供了多种类型的图表，如线图、散点图、柱状图、饼图等，适用于数据可视化和展示。
<br>
## 2. Matplotlib 基础
#### 2.1 导入 Matplotlib
```
import matplotlib.pyplot as plt
```
#### 2.2 绘制折线图
```
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)
plt.xlabel('X 轴')
plt.ylabel('Y 轴')
plt.title('简单折线图')
plt.show()
```
#### 2.3 散点图
```
plt.scatter(x, y)
plt.xlabel('X 轴')
plt.ylabel('Y 轴')
plt.title('散点图')
plt.show()
```

#### 2.4 柱状图
```
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 55]

plt.bar(categories, values)
plt.xlabel('类别')
plt.ylabel('值')
plt.title('柱状图')
plt.show()
```
<br>
## 3. 使用子图（Subplot）
子图允许您在一个图中绘制多个子图，方便进行比较和展示多个图表。
```
# 创建 2x2 的子图布局
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('子图 1')

plt.subplot(2, 2, 2)
plt.scatter(x, y)
plt.title('子图 2')

plt.subplot(2, 2, 3)
plt.bar(categories, values)
plt.title('子图 3')

plt.subplot(2, 2, 4)
plt.hist(values, bins=10)
plt.title('子图 4')

plt.tight_layout()  # 自动调整子图布局
plt.show()
```
<br>
## 4. 自定义图表样式
```
plt.plot(x, y, color='red', linestyle='dashed', marker='o', label='数据点')
plt.legend()
plt.grid()
plt.xlabel('X 轴')
plt.ylabel('Y 轴')
plt.title('自定义样式折线图')
plt.show()
```