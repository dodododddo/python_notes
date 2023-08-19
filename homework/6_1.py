from functools import reduce

def is_odd(x):
    return x % 2 == 1

def add(x, y):
    return x + y

def pow(x):
    return x ** 2

def mul(x, y):
    return x * y

def better(x, y):
    if x >= y:
        return x
    else:
        return y
    

l = [1, 2, 3, 4, 5]
l1 = filter(is_odd, l)
l2 = map(pow, l)
x3 = reduce(add, l)
x4 = reduce(mul, l)

x5 = reduce(better, l)

print(l1, l2, x3, x4)
