import os

year = input()

os.mkdir(os.curdir + '/' + year)

for i in range(1, 26):
    os.mkdir(os.curdir + '/' + year + '/' + f'day{i}')
    with open(f'{year}/day{i}/day{i}.py', 'w+') as pyfile:
        pyfile.write(f'''puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('{year}/day{i}/day{i}.txt', 'r') as file:
    puzzleinput = file.read()

def part1():
    print()

def part2():
    print()

part1()
part2()''')
    with open(f'{year}/day{i}/day{i}.txt', 'w+') as txtfile:
        continue