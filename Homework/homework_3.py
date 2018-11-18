#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:51:03 2018
@author: caggri, semih
"""
import random
import heapq
import collections
puzzleNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
final = puzzleNumbers.copy() #copy of puzzleNumbers
path = []
h = []

"""
create the 9-puzzle randomly and checks whether it is solvable
"""
def createGrid(puzzleNumbers):
    while puzzleNumbers[0] != 1: # 1 has to be in 0th position
        random.shuffle(puzzleNumbers)
    tmp = puzzleNumbers.copy()   # creates a temporary lisy from shuffled list
    tmp.remove(0)               # removes the 0
    count = checkSolvable(tmp)  # cheks solvability by using inversion method
    shuffle_status(count)

    return puzzleNumbers

def checkSolvable(arr):
    count = 0
    for i in range(8, 0, -1):
        for j in range(i-1, 0, -1):
            if arr[i] < arr[j]:
                count += 1
    return count

def shuffle_status(count):
    #print(count)
    if count % 2 == 0:
        print("Puzzle is solvable")
    else:
        print("Puzzle is not solvable, now shuffling again")
        while count % 2 != 0:
            random.shuffle(puzzleNumbers)
            while puzzleNumbers[0] != 1:
                random.shuffle(puzzleNumbers)
            tmp = puzzleNumbers.copy()
            tmp.remove(0)
            count = checkSolvable(tmp)
        print("Now the puzzle is solvable ")
        print(str(puzzleNumbers) + " inversion counts " + str(count))

def printGrid(nums):
    print("", nums[0], "\t", "X\t X\n", nums[1], "\t", nums[2], "\t", nums[3], "\n", nums[4], "\t", nums[5], "\t", nums[6], "\n", nums[7], "\t", nums[8], "\t", nums[9])

def distanceTiles(nums):
    emptyIndex = 0
    """
    count is the sum of the needed steps to reach final state for each number
    i.e. if we have nums[1] = 9
    9 have to move at least 4 steps from [0,0] to [2,2] in the 3x3 matrix
    we have 2 step at first (one for move 0->index1 and 1->index0)
    """
    count = 0
    if nums[0] != 0 :
        count += 1
    for i in range(1,10):
        x = (i-1)%3
        y = int((i-1)/3)
        value = nums[i]
        if value == 0:
            a = 0
            b = -1
        else:
            a = (value-1)%3
            b = int((value-1)/3)
        count = count + abs(x-a) + abs(y-b)

    for i in range(0,10):
        if nums[i] == 0:
            emptyIndex = i

    return count, emptyIndex

"""
selectSwitch is a function to move next step from the current state
we choose the next step by looking
    -   the "lastmove" value to prevent the loop
    -   possible moves and "count" values of each, calling "distanceTiles" function
    -   minimum of the count value of possible moves is choosen AS our next state
    -   if there is more than one minimum value, we choose one of them randomly
then calls "switch" function and prints out the new state
"""
def selectSwitch(numbers, currentPath):
    count, emptyIndex = distanceTiles(numbers)
    temp = numbers.copy()
    global path
    global h
    isOk = 0
    l = len(currentPath)
    #print("_______________current _________", currentPath)
    #print("_______________before h_________", h)

    if emptyIndex == 1:
        foo = list(currentPath)
        numbers1 = trySwitch(temp,1, 0)
        count1, empty = distanceTiles(numbers1)
        if count1 == 0 and numbers1 not in currentPath:
            isOk = 1
            foo.append(numbers1)
            path.append(foo)
            heapq.heappush(h, (count1+l, numbers1, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers2 = trySwitch(temp,1, 2)
        count2, empty = distanceTiles(numbers2)
        if numbers2 not in currentPath:
            isOk = 1
            foo.append(numbers2)
            path.append(foo)
            heapq.heappush(h, (count2+l, numbers2, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers3 = trySwitch(temp,1, 4)
        count3, empty = distanceTiles(numbers3)
        if numbers3 not in currentPath:
            isOk = 1
            foo.append(numbers3)
            path.append(foo)
            heapq.heappush(h, (count3+l, numbers3, foo))

    elif emptyIndex == 2:
        foo = list(currentPath)
        numbers1 = trySwitch(temp, 2, 1)
        count1, empty = distanceTiles(numbers1)
        if numbers1 not in currentPath:
            isOk = 1
            foo.append(numbers1)
            path.append(foo)
            heapq.heappush(h, (count1+l, numbers1, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers2 = trySwitch(temp, 2, 3)
        count2, empty = distanceTiles(numbers2)
        if numbers2 not in currentPath:
            isOk = 1
            foo.append(numbers2)
            path.append(foo)
            heapq.heappush(h, (count2+l, numbers2, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers3 = trySwitch(temp, 2, 5)
        count3, empty = distanceTiles(numbers3)
        if numbers3 not in currentPath:
            isOk = 1
            foo.append(numbers3)
            path.append(foo)
            heapq.heappush(h, (count3+l, numbers3, foo))

    elif emptyIndex == 3:
        foo = list(currentPath)
        numbers1 = trySwitch(temp, 3, 2)
        count1, empty = distanceTiles(numbers1)
        if numbers1 not in currentPath:
            isOk = 1
            foo.append(numbers1)
            path.append(foo)
            heapq.heappush(h, (count1+l, numbers1, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers2 = trySwitch(temp, 3, 6)
        count2, empty = distanceTiles(numbers2)
        if numbers2 not in currentPath:
            isOk = 1
            foo.append(numbers2)
            path.append(foo)
            heapq.heappush(h, (count2+l, numbers2, foo))

    elif emptyIndex == 4:
        foo = list(currentPath)
        numbers1 = trySwitch(temp, 4, 1)
        count1, empty = distanceTiles(numbers1)
        if numbers1 not in currentPath:
            isOk = 1
            foo.append(numbers1)
            path.append(foo)
            heapq.heappush(h, (count1+l, numbers1, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers2 = trySwitch(temp, 4, 5)
        count2, empty = distanceTiles(numbers2)
        if numbers2 not in currentPath:
            isOk = 1
            foo.append(numbers2)
            path.append(foo)
            heapq.heappush(h, (count2+l, numbers2, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers3 = trySwitch(temp, 4, 7)
        count3, empty = distanceTiles(numbers3)
        if numbers3 not in currentPath:
            isOk = 1
            foo.append(numbers3)
            path.append(foo)
            heapq.heappush(h, (count3+l, numbers3, foo))

    elif emptyIndex == 5:
        foo = list(currentPath)
        numbers1 = trySwitch(temp, 5, 2)
        count1, empty = distanceTiles(numbers1)
        if numbers1 not in currentPath:
            isOk = 1
            foo.append(numbers1)
            path.append(foo)
            heapq.heappush(h, (count1+l, numbers1, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers2 = trySwitch(temp, 5, 4)
        count2, empty = distanceTiles(numbers2)
        if numbers2 not in currentPath:
            isOk = 1
            foo.append(numbers2)
            path.append(foo)
            heapq.heappush(h, (count2+l, numbers2, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers3 = trySwitch(temp, 5, 6)
        count3, empty = distanceTiles(numbers3)
        if numbers3 not in currentPath:
            isOk = 1
            foo.append(numbers3)
            path.append(foo)
            heapq.heappush(h, (count3+l, numbers3, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers4 = trySwitch(temp, 5, 8)
        count4, empty = distanceTiles(numbers4)
        if numbers4 not in currentPath:
            isOk = 1
            foo.append(numbers4)
            path.append(foo)
            heapq.heappush(h, (count4+l, numbers4, foo))

    elif emptyIndex == 6:
        foo = list(currentPath)
        numbers1 = trySwitch(temp, 6, 3)
        count1, empty = distanceTiles(numbers1)
        if numbers1 not in currentPath:
            isOk = 1
            foo.append(numbers1)
            path.append(foo)
            heapq.heappush(h, (count1+l, numbers1, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers2 = trySwitch(temp, 6, 5)
        count2, empty = distanceTiles(numbers2)
        if numbers2 not in currentPath:
            isOk = 1
            foo.append(numbers2)
            path.append(foo)
            heapq.heappush(h, (count2+l, numbers2, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers3 = trySwitch(temp, 6, 9)
        count3, empty = distanceTiles(numbers3)
        if numbers3 not in currentPath:
            isOk = 1
            foo.append(numbers3)
            path.append(foo)
            heapq.heappush(h, (count3+l, numbers3, foo))

    elif emptyIndex == 7:
        foo = list(currentPath)
        numbers1 = trySwitch(temp, 7, 4)
        count1, empty = distanceTiles(numbers1)
        if numbers1 not in currentPath:
            isOk = 1
            foo.append(numbers1)
            path.append(foo)
            heapq.heappush(h, (count1+l, numbers1, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers2 = trySwitch(temp, 7, 8)
        count2, empty = distanceTiles(numbers2)
        if numbers2 not in currentPath:
            isOk = 1
            foo.append(numbers2)
            path.append(foo)
            heapq.heappush(h, (count2+l, numbers2, foo))

    elif emptyIndex == 8:
        foo = list(currentPath)
        numbers1 = trySwitch(temp, 8, 5)
        count1, empty = distanceTiles(numbers1)
        if numbers1 not in currentPath:
            isOk = 1
            foo.append(numbers1)
            path.append(foo)
            heapq.heappush(h, (count1+l, numbers1, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers2 = trySwitch(temp, 8, 7)
        count2, empty = distanceTiles(numbers2)
        if numbers2 not in currentPath:
            isOk = 1
            foo.append(numbers2)
            path.append(foo)
            heapq.heappush(h, (count2+l, numbers2, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers3 = trySwitch(temp, 8, 9)
        count3, empty = distanceTiles(numbers3)
        if numbers3 not in currentPath:
            isOk = 1
            foo.append(numbers3)
            path.append(foo)
            heapq.heappush(h, (count3+l, numbers3, foo))

    elif emptyIndex == 9:
        foo = list(currentPath)
        numbers1 = trySwitch(temp, 9, 6)
        count1, empty = distanceTiles(numbers1)
        if numbers1 not in currentPath:
            isOk = 1
            foo.append(numbers1)
            path.append(foo)
            heapq.heappush(h, (count1+l, numbers1, foo))

        temp = numbers.copy()
        foo = list(currentPath)
        numbers2 = trySwitch(temp, 9, 8)
        count2, empty = distanceTiles(numbers2)
        if numbers2 not in currentPath:
            isOk = 1
            foo.append(numbers2)
            path.append(foo)
            heapq.heappush(h, (count2+l, numbers2, foo))

    #print("..........................before path.......", path)
    #print("..........................currentPath.......", currentPath)


    path.remove(currentPath)
    if isOk != 1:
        path.append(currentPath)
    #print("..........................after path........", path)


    heapq.heapify(h)
    #print("_______________middle h_________", h)
    (cnt, next_state, next_path) = heapq.heappop(h)
    #print("_______________heappo  _________",(cnt, next_state, next_path))

    #print("_______________after  h_________", h)


    # path-e göre çalışacak
    #switch(numbers, emptyIndex, next_emptyIndex)

    return next_state, next_path


"""
def switch(nums, emptyIndex, switchIndex):
    global lastmove
    nums[emptyIndex], nums[switchIndex] = nums[switchIndex], nums[emptyIndex]
    lastmove = (emptyIndex, switchIndex)
    #print(lastmove)
    return nums
"""

def trySwitch(nums, emptyIndex, switchIndex):
    nums[emptyIndex], nums[switchIndex] = nums[switchIndex], nums[emptyIndex]
    return nums

def findMin(a, b):
    min = 0
    if a <= b:
        return a
    else:
        return b

""" main """
#puzzleNumbers = [1, 2, 5, 3, 4, 8, 6, 7, 9, 0]
#puzzleNumbers = [1, 2, 3, 6, 4, 5, 9, 0, 7, 8]
#puzzleNumbers = [1, 9, 0, 2, 3, 8, 7, 4, 5, 6] # 56 steps
def call_one_puzzle():
    global puzzleNumbers
    global emptyIndex
    global h
    global path
    currentPath = []

    createGrid(puzzleNumbers)

    print("------ start ------")
    printGrid(puzzleNumbers)
    print("-------------------")

    # adding the first state into heap


    currentPath.append(puzzleNumbers)
    path.append(currentPath)
    #print("^^^^^^^^^path^^^^^vvvvvvv", path)
    #print("^^^^^^^^^currentPath^^^^^", currentPath)

    i = 0
    while final != puzzleNumbers:
        #print("--- next step ---")
        #print(list(h))

        #print("~~~~~~~~~~~~~~~~~~~before currentPath~~~~", currentPath)
        puzzleNumbers, currentPath = selectSwitch(puzzleNumbers, currentPath)
        #print("~~~~~~~~~~~~~~~~~~~ after currentPath~~~~", currentPath)
        """
        i += 1
        if i>10000:
            print("...not solved in 10000 steps - trying again...")
            i = 0
            createGrid(puzzleNumbers)

            print("------ start ------")
            printGrid(puzzleNumbers)
            print("-------------------")
        """
        #printGrid(puzzleNumbers)
        #print("^^^^^^^^^path^^^^^", path)
        #print("^^^^^^^^^currentPath^^^^^", currentPath)
        #print("-------------------")
        #print(len(currentPath))


    #print("------ final ------")
    #printGrid(puzzleNumbers)
    #print("-------------------")
    for item in currentPath:
        printGrid(item)
        print("-------------------")

    print("...it takes ", len(currentPath), "steps")

for i in range(1,11):
    print("\n----- ##### ----- THE ", i, ". PUZZLE LOADING ----- ##### -----")
    call_one_puzzle()
