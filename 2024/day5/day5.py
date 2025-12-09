puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day5/day5.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

testinput = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def getmiddlepage(list :list) -> int:
    if len(list) % 2 == 1:
        return int(list[int((len(list) -1) / 2)])
    return int(list[int(len(list) / 2)])

def haspair(orderlist :list, updatex :str, updatey :str) -> bool:
    for order in orderlist:
        if updatex == order[0] and updatey == order[1]:
            return True
    return False

def correctorder(orderlist :list, updatelist :list) -> bool:
    for i in range(len(updatelist) -1):
        if not haspair(orderlist, updatelist[i], updatelist[i+1]):
            return False
    return True

def fixupdate(orderlist :list, updatelist :list) -> list:
    updatecopy = updatelist.copy()
    while not correctorder(orderlist, updatecopy):
        for i in range(len(updatecopy) -1):
            if not haspair(orderlist, updatecopy[i], updatecopy[i+1]):
                updatecopy[i], updatecopy[i +1] = updatecopy[i +1], updatecopy[i]
    return updatecopy
            

def part1():
    input = puzzleinput
    pageorderlist = []
    updatelist = []
    orders, updates = input.split('\n\n')
    for pageorder in orders.split('\n'):
        pagex, pagey = pageorder.split('|')
        pageorderlist.append([pagex, pagey])
    for pageupdate in updates.split('\n'):
        stringnums = pageupdate.split(',')
        helparr = []
        for stringnum in stringnums:
            helparr.append(stringnum)
        updatelist.append(helparr)
    middlepagetotal = 0
    for update in updatelist:
        if correctorder(pageorderlist, update):
            middlepagetotal += getmiddlepage(update)
    print(middlepagetotal)

def part2():
    input = puzzleinput
    pageorderlist = []
    updatelist = []
    orders, updates = input.split('\n\n')
    for pageorder in orders.split('\n'):
        pagex, pagey = pageorder.split('|')
        pageorderlist.append([pagex, pagey])
    for pageupdate in updates.split('\n'):
        stringnums = pageupdate.split(',')
        helparr = []
        for stringnum in stringnums:
            helparr.append(stringnum)
        updatelist.append(helparr)
    tofixupdates = []
    for update in updatelist:
        if not correctorder(pageorderlist, update):
            tofixupdates.append(update)
    middlepagetotal = 0
    for update in tofixupdates:
        middlepagetotal += getmiddlepage(fixupdate(pageorderlist, update))
    print(middlepagetotal)
    print()

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")