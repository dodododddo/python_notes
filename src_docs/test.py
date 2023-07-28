str = 'hello'
num = 0
empty = []

if len(str):
    print(str)

if str:
    print(str)

if num:
    print(num)

if empty:
    print(len(empty))

for idx, letter in enumerate(str):
    print(idx, letter)