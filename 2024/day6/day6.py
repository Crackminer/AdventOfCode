puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day6/day6.txt', 'r') as file:
    puzzleinput = file.read()

def makestep(field :list) -> None:
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '>':
                if j +1 < len(field[i]) and field[i][j +1] != '#':
                    field[i] = field[i][:j] + 'X' + field[i][j+1:]
                    field[i] = field[i][:j+1] + '>' + field[i][j+2:]
                elif j +1 < len(field[i]):# and field[i][j +1] == '#':
                    field[i] = field[i][:j] + 'v' + field[i][j+1:]
                else:
                    field[i] = field[i][:j] + 'X' + field[i][j+1:]
                return
            elif field[i][j] == '<':
                if j -1 >= 0 and field[i][j -1] != '#':
                    field[i] = field[i][:j] + 'X' + field[i][j+1:]
                    field[i] = field[i][:j-1] + '<' + field[i][j:]
                elif j -1 < len(field[i]):# and field[i][j -1] == '#':
                    field[i] = field[i][:j] + '^' + field[i][j+1:]
                else:
                    field[i] = field[i][:j] + 'X' + field[i][j+1:]
                return
            elif field[i][j] == '^':
                if i -1 >= 0 and field[i -1][j] != '#':
                    field[i] = field[i][:j] + 'X' + field[i][j+1:]
                    field[i -1] = field[i -1][:j] + '^' + field[i -1][j+1:]
                elif i -1 < len(field[i]):# and field[i -1][j] == '#':
                    field[i] = field[i][:j] + '>' + field[i][j+1:]
                else:
                    field[i] = field[i][:j] + 'X' + field[i][j+1:]
                return
            elif field[i][j] == 'v':
                if i +1 < len(field) and field[i +1][j] != '#':
                    field[i] = field[i][:j] + 'X' + field[i][j+1:]
                    field[i +1] = field[i +1][:j] + 'v' + field[i +1][j+1:]
                elif i +1 < len(field):# and field[i +1][j] == '#':
                    field[i] = field[i][:j] + '<' + field[i][j+1:]
                else:
                    field[i] = field[i][:j] + 'X' + field[i][j+1:]
                return

def gameended(field :list) -> bool:
    for line in field:
        for char in line:
            if char == '<' or char == '>' or char == '^' or char == 'v':
                return False
    return True

def countX(field :list) -> int:
    count = 0
    for line in field:
        for char in line:
            if char == 'X':
                count += 1
    return count

def part1():
    input = puzzleinput
    field = []
    for line in puzzleinput.split('\n'):
        field.append(line)
    while not gameended(field):
        makestep(field)
    print(countX(field))

def part2():
    print()

part1()
part2()