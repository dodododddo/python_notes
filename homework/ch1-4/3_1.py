src = input('请输入字符串:')
target = input('请输入目标字符:')

pos = -1
for idx, letter in enumerate(src):
    if letter == target:
        pos = idx
        break
# 等价于:
# pos = src.find(target)

if pos >= 0:
    print(f'查找成功，pos = {pos}')
else:
    print('查找失败')
    
    

    