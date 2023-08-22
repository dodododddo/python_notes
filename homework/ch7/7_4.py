'''
练习题：创建订单和商品类

问题描述：
创建两个类，Order（订单）和 Product（商品），它们之间可以协作以创建订单并计算订单总额。

    创建一个 Product 类，具有以下属性：
        商品名称（name）
        商品价格（price）

    创建一个 Order 类，具有以下功能：
        初始化方法 __init__(self)，用于初始化一个空订单。
        方法 add_product(self, product, quantity)，接受一个商品对象和数量，将商品添加到订单中。
        方法 calculate_total(self)，计算订单中所有商品的总价。
        方法 display_order(self)，显示订单中的商品列表及其数量。

要求：

    在 calculate_total 方法中，考虑每种商品的价格和数量来计算订单总价。
'''

class Product:
    def __init__(self, name, price):
        # your code
        pass

class Order:
    def __init__(self):
        # your code
        pass
        
    def add_product(self, product, quantity):
        # your code
        pass
            
    def calculate_total(self):
        # your code
        pass
    
    def display_order(self):
        # your code
        pass



# 创建商品实例
product1 = Product("Apple", 1)
product2 = Product("Banana", 0.5)
product3 = Product("Orange", 0.75)

# 创建订单实例
order = Order()

# 添加商品到订单
order.add_product(product1, 3)
order.add_product(product2, 2)
order.add_product(product3, 4)

# 显示订单详情
order.display_order()
total_price = order.calculate_total()
print(f"Total price of the order: ${total_price:.2f}")


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class Order:
#     def __init__(self):
#         self.products = {}  # 使用字典来存储订单中的商品，键是商品对象，值是数量
        
#     def add_product(self, product, quantity):
#         if product in self.products:
#             self.products[product] += quantity
#         else:
#             self.products[product] = quantity
            
#     def calculate_total(self):
#         total = 0
#         for product, quantity in self.products.items():
#             total += product.price * quantity
#         return total
    
#     def display_order(self):
#         print("Order details:")
#         for product, quantity in self.products.items():
#             print(f"{product.name} x{quantity} (${product.price * quantity:.2f} each)")
