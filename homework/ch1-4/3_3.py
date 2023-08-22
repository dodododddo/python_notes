src = input('请输入字符串:')
target = input('请输入目标字符串:')

src_len = len(src)
target_len = len(target)

pos = -1
for idx in range(src_len - target_len + 1):
    if src[idx: idx + target_len] == target:
        pos = idx
        
if pos >= 0:
    print(f'查找成功，pos = {pos}')
else:
    print('查找失败')