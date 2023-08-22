length = int(input('请设置列表长度:'))
nums = [int(input(f'请输入列表第{i}位:')) for i in range(length)]
factor = int(input('请输入乘数:'))

res = [num * factor for num in nums]

print(f'结果为{res}')