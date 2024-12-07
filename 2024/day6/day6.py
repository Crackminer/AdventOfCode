puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day6/day6.txt', 'r') as file:
    puzzleinput = file.read()

# my part 2 was not working, once again thanks to TessFerrandez i was able to finish this. Part 1 i was able to finish myself though, Luckily.
# Github of TessFerrandez: https://github.com/TessFerrandez/AdventOfCode-Python/blob/develop/2024/day6.py

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
    for line in input.split('\n'):
        field.append(line)
    while not gameended(field):
        makestep(field)
    print(countX(field))

def parse(data):
    data = data.splitlines()
    obstacles = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                obstacles.add((x, y))
            elif char == '^':
                start = (x, y)
    width = len(data[0])
    height = len(data)
    return obstacles, start, width, height


def get_guard_positions(obstacles, start, width, height):
    visited = set()
    x, y = start
    direction = -1j

    while 0 <= x < width and 0 <= y < height:
        visited.add((x, y))
        next_pos = (x + direction.real, y + direction.imag)
        while next_pos in obstacles:
            # turn right
            direction = direction * 1j
            next_pos = (x + direction.real, y + direction.imag)
        x, y = next_pos

    return visited


def is_loop(obstacles, start, width, height):
    visited = set()
    x, y = start
    direction = -1j

    while 0 <= x < width and 0 <= y < height:
        if ((x, y), direction) in visited:
            return True
        visited.add(((x, y), direction))
        next_pos = (x + direction.real, y + direction.imag)
        while next_pos in obstacles:
            # turn right
            direction = direction * 1j
            next_pos = (x + direction.real, y + direction.imag)
        x, y = next_pos

    return False

def part2(obstacles, start, width, height):
    guard_positions = get_guard_positions(obstacles, start, width, height)
    guard_positions.remove(start)

    good_positions = set()
    i = 0
    for position in guard_positions:
        i += 1
        if i % 100 == 0:
            print(".", end="")
        obstacles.add(position)
        if is_loop(obstacles, start, width, height):
            good_positions.add(position)
        obstacles.remove(position)
    print()

    return len(good_positions)


def test():
    data = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
    obstacles, start, width, height = parse(data)
    assert part2(obstacles, start, width, height) == 6

test()
data = puzzleinput
obstacles, start, width, height = parse(data)
print('Part2:', part2(obstacles, start, width, height))

part1()