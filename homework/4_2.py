table = {'John': 98, 'Cindy': 99, 'Deft': 76, 'Salas': 76}

keys = [key for key in table]
values = [value for value in table.values()]
values = list(set(values))

keys, values = *zip()
print(f'键:{keys}, 已去重的值:{values}')