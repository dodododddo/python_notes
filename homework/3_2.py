a = int(input('请输入第一个整数:'))
b = int(input('请输入第二个整数:'))
x, y = a, b 
while(y > 0):
    x, y = y, x % y

gcd = x
lcm = a * b // gcd
print(f'gcd = {gcd}, lcm = {lcm}')