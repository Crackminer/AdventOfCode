puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day18/day18.txt', 'r') as file:
    puzzleinput = file.read()
# fuck this, idk why it isnt working but somehow it isnt working
def initialstate(input :str) -> list:
    list = []
    for line in input.split('\n'):
        myline = []
        for char in line:
            if char == '#':
                myline.append(True)
            else:
                myline.append(False)
        list.append(myline)
    return list

def getneighbours(state :list, i :int, j :int) -> int:
    count = 0
    if i == 0:
        if j == 0:
            #upper corner
            # A B . . .
            # C D . . .
            # . . . . .
            # . . . . .
            # . . . . .
            
            # C
            if state[i+1][j]:
                count += 1
            # B
            if state[i][j+1]:
                count += 1
            # D
            if state[i+1][j+1]:
                count += 1
            return count
        elif j == len(state[i]) -1:
            #upper corner
            # . . . B A
            # . . . D C
            # . . . . .
            # . . . . .
            # . . . . .

            # C
            if state[i+1][j]:
                count += 1
            # B
            if state[i][j-1]:
                count += 1
            # D
            if state[i+1][j-1]:
                count += 1
            return count
        else:
            # upper side
            # . B A C .
            # . D E F .
            # . . . . .
            # . . . . .
            # . . . . .

            # B
            if state[i][j-1]:
                count += 1
            # c
            if state[i+1][j+1]:
                count += 1
            # D
            if state[i+1][j-1]:
                count += 1
            # E
            if state[i+1][j]:
                count += 1
            # F
            if state[i+1][j+1]:
                count += 1
            return count
    elif i == len(state) -1:
        if j == 0:
            #lower corner
            # . . . . .
            # . . . . .
            # . . . . .
            # C D . . .
            # A B . . .

            # C
            if state[i-1][j]:
                count += 1
            # B
            if state[i][j+1]:
                count += 1
            # C
            if state[i-1][j+1]:
                count += 1
            return count
        elif j == len(state[i]) -1:
            #lower corner
            # . . . . .
            # . . . . .
            # . . . . .
            # . . . D C
            # . . . B A

            # C
            if state[i-1][j]:
                count += 1
            # B
            if state[i][j-1]:
                count += 1
            # D
            if state[i-1][j-1]:
                count += 1
            return count
        else:
            #lower side
            # . . . . .
            # . . . . .
            # . . . . .
            # . D E F .
            # . B A C .

            # E
            if state[i-1][j]:
                count += 1
            # D
            if state[i-1][j-1]:
                count += 1
            # F
            if state[i-1][j+1]:
                count += 1
            # C
            if state[i][j+1]:
                count += 1
            # B
            if state[i][j-1]:
                count += 1
            return count
    else:
        if j == 0:
            #left side
            # . . . . .
            # B C . . .
            # A D . . .
            # E F . . .
            # . . . . .

            # C
            if state[i-1][j+1]:
                count += 1
            # D
            if state[i][j+1]:
                count += 1
            # F
            if state[i+1][j+1]:
                count += 1
            # B
            if state[i-1][j]:
                count += 1
            # E
            if state[i+1][j]:
                count += 1
            return count
        elif j == len(state[i]) -1:
            #right side
            # . . . . .
            # . . . C B
            # . . . D A
            # . . . E F
            # . . . . .

            # C
            if state[i-1][j-1]:
                count += 1
            # D
            if state[i][j-1]:
                count += 1
            # E
            if state[i+1][j-1]:
                count += 1
            # B
            if state[i-1][j]:
                count += 1
            # F
            if state[i+1][j]:
                count += 1
            return count
        else:
            #middle
            # . . . . .
            # . B C D .
            # . E A F .
            # . G H I .
            # . . . . .

            # B
            if state[i-1][j-1]:
                count += 1
            # C
            if state[i-1][j]:
                count += 1
            # D
            if state[i-1][j+1]:
                count += 1
            # E
            if state[i][j-1]:
                count += 1
            # F
            if state[i][j+1]:
                count += 1
            # G
            if state[i+1][j-1]:
                count += 1
            # H
            if state[i+1][j]:
                count += 1
            # I
            if state[i+1][j+1]:
                count += 1
            return count

def makestep(state :list) -> list:
    newstate = []
    for i in range(len(state)):
        newline = []
        for j in range(len(state[i])):
            neighbours = getneighbours(state, i, j)
            if state[i][j]:
                if neighbours < 2 or neighbours > 3:
                    newline.append(False)
                else:
                    newline.append(True)
            else:
                if neighbours == 3:
                    newline.append(True)
                else:
                    newline.append(False)
        newstate.append(newline)
    return newstate

def countlights(state :list) -> int:
    count = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j]:
                count += 1
    return count

def part1():
    state = initialstate(puzzleinput)
    for i in range(100):
        state = makestep(state)
    print(countlights(state))

def part2():
    print()

part1()
part2()

# since my solution doesnt work i didnt bother for part 2, here is the solution of TessFerrandez: https://github.com/TessFerrandez/AdventOfCode-Python/blob/develop/2015/day18.py


import numpy as np
from copy import deepcopy


def parse_input(filename: str) -> np.array:
    lines = [line.strip() for line in open(filename).readlines()]
    size = len(lines)
    grid = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            grid[i][j] = 1 if lines[i][j] == '#' else 0
    return grid


def inc(grid: np.array, corner_lock: bool):
    old_grid = deepcopy(grid)
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if corner_lock and ((row == 0 and col == 0) or (row == 0 and col == size - 1) or (row == size - 1 and col == 0) or (row == size - 1 and col == size - 1)):
                continue
            adjacent = np.sum(old_grid[max(row - 1, 0):min(row + 2, size), max(col - 1, 0):min(col + 2, size)])
            if old_grid[row][col] == 1 and adjacent not in [3.0, 4.0]:
                grid[row][col] = 0
            elif old_grid[row][col] == 0 and adjacent == 3.0:
                grid[row][col] = 1


def part1(grid: np.array, iterations: int) -> int:
    for i in range(iterations):
        inc(grid, False)
    return int(np.sum(grid))


def part2(grid: np.array, iterations: int) -> int:
    size = len(grid)
    grid[0][0] = 1
    grid[0][size - 1] = 1
    grid[size - 1][0] = 1
    grid[size - 1][size - 1] = 1
    for i in range(iterations):
        inc(grid, True)
    return int(np.sum(grid))


def main():
    grid = parse_input('2015/day18/day18.txt')
    print(f'Part 1: {part1(grid, 100)}')
    grid = parse_input('2015/day18/day18.txt')
    print(f'Part 2: {part2(grid, 100)}')


if __name__ == "__main__":
    main()