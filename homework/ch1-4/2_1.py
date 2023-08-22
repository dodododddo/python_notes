id = input('请输入身份证号码:')

# assert(len(id) == 18)
year = int(id[6: 10])
month = int(id[10: 12])
day = int(id[12: 14])

print(f'year = {year}, month = {month}, day = {day}')