import os

year = input()

os.mkdir(os.curdir + '/' + year)

# Account for only having 12 Riddles per year starting in 2025. Assuming each riddle will be offset 2 days and not generated each day until the 12th
for i in range(1, 13):
    os.mkdir(os.curdir + '/' + year + '/' + f'day{i}')
    with open(f'{year}/day{i}/day{i}.py', 'w+') as pyfile:
        pyfile.write(f'''puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('{year}/day{i}/day{i}.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

testinput = """"""

def part1():
    # puzzleinput = testinput
    print()

def part2():
    # puzzleinput = testinput
    print()

print(f"{{datetime.now()}}: Started executing part1.")
part1()
print(f"{{datetime.now()}}: Ended executing part1.")
print(f"{{datetime.now()}}: Started executing part2.")
part2()
print(f"{{datetime.now()}}: Ended executing part2.")''')
    with open(f'{year}/day{i}/day{i}.txt', 'w+') as txtfile:
        continue