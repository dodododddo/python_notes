'''
练习题：创建购物车类

问题描述：
创建一个 ShoppingCart 类，该类应具有以下功能：

    初始化方法 __init__(self)，用于初始化购物车。
    方法 add_item(self, item_name, item_price)，接受商品名称 item_name 和价格 item_price，将商品添加到购物车。
    方法 remove_item(self, item_name)，接受商品名称 item_name，从购物车中删除该商品。
    方法 calculate_total(self)，计算购物车中所有商品的总价。
    方法 display_items(self)，显示购物车中所有商品的名称和价格。

要求：

    考虑可能会有重复的商品。
    在 calculate_total 方法中，考虑将每个商品的价格相加以计算总价。
'''
class ShoppingCart:
    def __init__(self):
        # your code
        pass
        
    def add_item(self, item_name, item_price):
        # your code
        pass
            
    def remove_item(self, item_name):
        # your code
        pass
    def calculate_total(self):
        # your code
        pass
    
    def display_items(self):
        # your code
        pass


# 创建购物车实例
cart = ShoppingCart()

# 调用方法
cart.add_item("Apple", 1)
cart.add_item("Banana", 0.5)
cart.add_item("Apple", 1)  # 测试重复商品
cart.remove_item("Banana")
cart.add_item("Orange", 0.75)
cart.display_items()
total_price = cart.calculate_total()
print(f"Total price of items in the cart: ${total_price}")





# class ShoppingCart:
#     def __init__(self):
#         self.items = {}  # 使用字典来存储商品，键是商品名称，值是价格
        
#     def add_item(self, item_name, item_price):
#         if item_name in self.items:
#             print(f"{item_name} is already in the cart.")
#         else:
#             self.items[item_name] = item_price
#             print(f"Added {item_name} to the cart. Price: ${item_price}")
            
#     def remove_item(self, item_name):
#         if item_name in self.items:
#             removed_price = self.items.pop(item_name)
#             print(f"Removed {item_name} from the cart. Price: ${removed_price}")
#         else:
#             print(f"{item_name} is not in the cart.")
            
#     def calculate_total(self):
#         total = sum(self.items.values())
#         return total
    
#     def display_items(self):
#         print("Items in the cart:")
#         for item_name, item_price in self.items.items():
#             print(f"{item_name}: ${item_price}")