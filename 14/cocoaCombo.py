from __future__ import print_function


def main():
    #Part 1
    cocoaList = [3, 7]
    elfOne = 0
    elfTwo = 1
    while (len(cocoaList) < 47811):
        cocoaList = newRecipe(cocoaList, elfOne, elfTwo)
        elfOne = moveElf(cocoaList, elfOne)
        elfTwo = moveElf(cocoaList, elfTwo)
    print("Part 1 answer: ", end="")
    printRecipes(cocoaList, elfOne, elfTwo)

    #Part 2
    cocoaList = [3, 7]
    elfOne = 0
    elfTwo = 1
    foundSequence = False
    while len(cocoaList) < 30000000:
        cocoaList = newRecipe(cocoaList, elfOne, elfTwo)
        elfOne = moveElf(cocoaList, elfOne)
        elfTwo = moveElf(cocoaList, elfTwo)


    print("Part 2 answer: " + str(checkForSequence(cocoaList, [0, 4, 7, 8, 0, 1])))


def newRecipe(list, elfOne, elfTwo):
    score = list[elfOne] + list[elfTwo]
    score = str(score)

    if len(score) > 1:
        list.append(int(score[0]))
        list.append(int(score[1]))
    else:
        list.append(int(score))

    return list

def moveElf(list, elf):
    elfMoves = list[elf] + 1
    while elfMoves > 0:
        elf += 1
        if elf == len(list):
            elf = 0
        elfMoves -= 1
    return elf

#def checkForSequence(list):
    #return lambda x: any([0,4,7,8,0,1] == x[offset:offset + 3] for offset in range(len(x)))

def checkForSequence(source, target, start=0, end=None):
    """Naive search for target in source."""
    m = len(source)
    n = len(target)
    if end is None:
        end = m
    else:
        end = min(end, m)
    if n == 0 or (end-start) < n:
        # target is empty, or longer than source, so obviously can't be found.
        return False

    x = range(start, end-n+1)
    for i in x:
        if source[i:i+n] == target:
            return i
    return False

def printRecipes(list, elfOne, elfTwo):
    for each in range(47801, len(list)):
        if elfOne == each:
            print("(" + str(list[each]) + ")", end=" ")
        elif elfTwo == each:
            print("[" + str(list[each]) + "]", end=" ")
        else:
            print(" " + str(list[each]), end="  ")
    print("")

if __name__ == "__main__":
    main()