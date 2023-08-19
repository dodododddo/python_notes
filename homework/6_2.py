import time
from functools import wraps

# 装饰器：在函数执行前后打印消息
def print_message(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("在函数执行前打印消息")
        result = func(*args, **kwargs)
        print("在函数执行后打印消息")
        return result
    return wrapper

# 装饰器：计算函数执行时间并打印
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数执行时间：{end_time - start_time}秒")
        return result
    return wrapper

# 装饰器：在特定条件下执行函数
def conditional_execution(condition):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                print("函数未执行，条件不满足")
        return wrapper
    return decorator

# 使用装饰器
@print_message
@measure_time
def example_function():
    time.sleep(2)
    print("函数执行中")

@conditional_execution(condition=True)
def conditional_function():
    print("函数执行了")

# 调用被装饰的函数
example_function()
conditional_function()
