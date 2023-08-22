''' 
问题描述：
创建一个 BankAccount 类，该类应具有以下功能：

    初始化方法 __init__(self, owner, balance)，其中 owner 是账户持有人的姓名，balance 是初始余额。
    方法 deposit(self, amount)，接受一个存款金额 amount，并将其添加到余额中。
    方法 withdraw(self, amount)，接受一个取款金额 amount，如果余额足够，从余额中扣除该金额。
    方法 display_balance(self)，用于显示账户持有人姓名和当前余额。
'''

class BankAccount:
    def __init__(self, owner, balance=0):
        # your code
        pass
        
    def deposit(self, amount):
        # your code
        pass
    
    def withdraw(self, amount):
        # your code
        pass
    
    def display_balance(self):
        # your code
        pass


# 创建账户实例
account1 = BankAccount("Alice", 1000)

# 调用方法
account1.display_balance()
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()




# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount}. New balance: ${self.balance}")
#         else:
#             print("Deposit amount must be greater than 0.")
            
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ${amount}. New balance: ${self.balance}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount.")
            
#     def display_balance(self):
#         print(f"Account owner: {self.owner}\nCurrent balance: ${self.balance}")
