puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2025/day6/day6.txt', 'r') as file:
    puzzleinput = file.read()

testinput = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

def part1():
    #puzzleinput = testinput
    nums = []
    ops = []
    nums2tmp = []
    # gather input line by line
    for line in puzzleinput.splitlines():
        numstmp = []
        for word in line.split(' '):
            if word == '':
                continue
            if word.isdecimal():
                numstmp.append(int(word))
            else:
                ops.append(word)
        if len(numstmp) != 0:
            nums2tmp.append(numstmp)

    # transform nums from line by line to actual approach col by col
    for i in range(len(ops)):
        tmpnum = []
        for numstmp in nums2tmp:
            tmpnum.append(numstmp[i])
        nums.append(tmpnum)

    # calculate the approach
    truesum = 0
    for i in range(len(nums)):
        numsum = 1 if ops[i] == '*' else 0
        for num in nums[i]:
            if ops[i] == '*':
                numsum *= num
            else:
                numsum += num
        truesum += numsum
    print(truesum)

def part2():
    #puzzleinput = testinput

    lines = puzzleinput.splitlines()
    # cheating in one char at the end of each line as i do not iterate from high to low but from low to high and already have my op, + im too lazy to reverse my approach
    for i in range(len(lines)):
        lines[i] += ' '

    truesum = 0
    numbers = []
    op = ''
    for i in range(len(lines[0])):
        allSpace = True
        for j in range(len(lines)):
            if lines[j][i] != ' ':
                allSpace = False
            pass
        if allSpace:
            numsum = 1 if op == '*' else 0
            for number in numbers:
                nu = int(number.strip())
                if op == '*':
                    numsum *= nu
                else:
                    numsum += nu
            truesum += numsum    
            op = ''
            numbers = []
        else:
            num = ""
            for k in range(len(lines)):
                if k == len(lines)-1:
                    if lines[k][i] != ' ' and lines[k][i] != '\n':
                        op = lines[k][i]
                else:
                    num += lines[k][i]
            numbers.append(num)
    print(truesum)

part1()
part2()