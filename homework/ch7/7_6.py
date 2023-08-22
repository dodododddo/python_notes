'''
练习题：创建形状类和派生类

问题描述：
创建一个 Shape（形状）基类和两个派生类 Circle（圆）和 Rectangle（矩形）。

    创建一个 Shape 基类，具有以下属性和方法：
        属性：颜色（color）
        方法 get_area(self)，返回形状的面积（默认为0）。

    创建一个 Circle 派生类，具有以下属性和方法：
        继承 Shape 基类。
        属性：半径（radius）
        重写方法 get_area(self)，根据半径计算并返回圆的面积。

    创建一个 Rectangle 派生类，具有以下属性和方法：
        继承 Shape 基类。
        属性：宽度（width）和高度（height）
        重写方法 get_area(self)，根据宽度和高度计算并返回矩形的面积。
'''

class Shape:
    def __init__(self, color):
        # your code
        pass
        
    def get_area(self):
        # your code
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        # your code
        pass
        
    def get_area(self):
        # your code
        pass

class Rectangle(Shape):
    def __init__(self, color, width, height):
        # your code
        pass
    def get_area(self):
        # your code
        pass

# 创建圆和矩形实例
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)

# 打印圆和矩形的面积
print(f"Circle area: {circle.get_area():.2f}")
print(f"Rectangle area: {rectangle.get_area()}")


# class Shape:
#     def __init__(self, color):
#         self.color = color
        
#     def get_area(self):
#         return 0

# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.radius = radius
        
#     def get_area(self):
#         return 3.14159 * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.width = width
#         self.height = height
        
#     def get_area(self):
#         return self.width * self.height