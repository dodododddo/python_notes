a = int(input('请输入第一个整数:'))
b = int(input('请输入第二个整数:'))

c = a * b
length = len(str(c))
num = c % 10

print(f'length = {length}, num = {num}')