puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day2/day2.txt', 'r') as file:
    puzzleinput = file.read()

def part1():
    totalwrappingpaper = 0
    for line in puzzleinput.split('\n'):
        dimensions = line.split('x')
        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])

        s1 = length * width
        s2 = width * height
        s3 = length * height

        totalwrappingpaper += s1 + s1 + s2 + s2 + s3 + s3

        min = s1
        if s2 < min:
            min = s2
        if s3 < min:
            min = s3
        
        totalwrappingpaper += min

    print(f'The total amount of wrapping paper needed is {totalwrappingpaper}')

def part2():
    totalribbon = 0
    for line in puzzleinput.split('\n'):
        dimensions = line.split('x')
        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])

        smallest = 1000000000
        secondsmallest = 2000000000

        if length < smallest:
            secondsmallest = smallest
            smallest = length
        elif length < secondsmallest:
            secondsmallest = length
        
        if width < smallest:
            secondsmallest = smallest
            smallest = width
        elif width < secondsmallest:
            secondsmallest = width
        
        if height < smallest:
            secondsmallest = smallest
            smallest = height
        elif height < secondsmallest:
            secondsmallest = height

        totalribbon += smallest + smallest + secondsmallest + secondsmallest

        totalribbon += length * width * height


    print(f'The total amount of ribbon needed is {totalribbon}')

part1()
part2()