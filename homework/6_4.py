def infinite_fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 创建生成器
fibonacci_gen = infinite_fibonacci_generator()

# 生成并输出斐波那契数列的前 10 个数
for i in range(10):
    print(next(fibonacci_gen))
