#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:51:03 2018

@author: caggri, semih
"""
import random
puzzleNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
final = list(puzzleNumbers) #copy of puzzleNumbers

lastmove = (0,1) #global lastmove variable initially 0,1

"""
create the 9-puzzle randomly and checks whether it is solvable
"""
def createGrid(puzzleNumbers):
    while puzzleNumbers[0] != 1: # 1 has to be in 0th position
        random.shuffle(puzzleNumbers)
    tmp = list(puzzleNumbers)  # creates a temporary lisy from shuffled list
    tmp.remove(0)  # removes the 0
    count = checkSolvable(tmp) # cheks solvability by using inversion method
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
            tmp = list(puzzleNumbers)
            tmp.remove(0)
            count = checkSolvable(tmp)
        print("Now the puzzle is solvable ")
        print(str(puzzleNumbers) + " inversion counts " + str(count))

def printGrid(nums):
    print("", nums[0], "\t", "X\t X\n", nums[1], "\t", nums[2], "\t", nums[3], "\n", nums[4], "\t", nums[5], "\t", nums[6], "\n", nums[7], "\t", nums[8], "\t", nums[9])

def placedTiles(nums):
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
    -   possible moves and "count" values of each, calling "placedTiles" function
    -   minimum of the count value of possible moves is choosen AS our next state
    -   if there is more than one minimum value, we choose one of them randomly
then calls "switch" function and prints out the new state
"""
def selectSwitch(numbers, emptyIndex):
    temp = list(numbers)
    #switchIndex = -1
    global lastmove

    if emptyIndex == 1:
        numbers1 = trySwitch(temp,1, 0)
        count1, emptyIndex = placedTiles(numbers1)

        temp = list(numbers)
        numbers2 = trySwitch(temp,1, 2)
        count2, emptyIndex = placedTiles(numbers2)

        temp = list(numbers)
        numbers3 = trySwitch(temp,1, 4)
        count3, emptyIndex = placedTiles(numbers3)

        y = findMin(count2,count3)

        if count1 == 0:
            switch(numbers, 1, 0)
        elif lastmove == (2,1):
            switch(numbers, 1, 4)
        elif lastmove == (4,1):
            switch(numbers, 1, 2)
        else:
            if y == count2 and y == count3:
                print("random", y)
                a = random.choice([2,4])
                switch(numbers, 1, a)
            elif y == count2:
                switch(numbers, 1, 2)
            elif y == count3:
                switch(numbers, 1, 4)
        #printGrid(numbers)

    elif emptyIndex == 2:
        numbers1 = trySwitch(temp, 2, 1)
        count1, emptyIndex = placedTiles(numbers1)

        temp = list(numbers)
        numbers2 = trySwitch(temp, 2, 3)
        count2, emptyIndex = placedTiles(numbers2)

        temp = list(numbers)
        numbers3 = trySwitch(temp, 2, 5)
        count3, emptyIndex = placedTiles(numbers3)

        if lastmove == (1,2):
            x =  findMin(count2, count3)
            if (x == count2 and x == count3):
                a = random.choice([3,5])
                switch(numbers, 2, a)
            elif x == count2:
                switch(numbers, 2, 3)
            elif x == count3:
                switch(numbers, 2, 5)
        elif lastmove == (3,2):
            x =  findMin(count1, count3)
            if (x == count1 and x == count3):
                a = random.choice([1,5])
                switch(numbers, 2, a)
            elif x == count1:
                switch(numbers, 2, 1)
            elif x == count3:
                switch(numbers, 2, 5)
        elif lastmove == (5,2):
            x =  findMin(count1, count2)
            if (x == count1 and x == count2):
                a = random.choice([1,3])
                switch(numbers, 2, a)
            elif x == count1:
                switch(numbers, 2, 1)
            elif x == count2:
                switch(numbers, 2, 3)
        else:
            x = findMin(count1, findMin(count2, count3))
            if x == count1 and x == count2 and x == count3:
                a = random.choice([1,3,5])
                switch(numbers, 2, a)
            elif x == count1 and x == count2:
                a = random.choice([1,3])
                switch(numbers, 2, a)
            elif x == count1 and x == count3:
                a = random.choice([1,5])
                switch(numbers, 2, a)
            elif x == count2 and x == count3:
                a = random.choice([3,5])
                switch(numbers, 2, a)
            elif x == count1:
                switch(numbers, 2, 1)
            elif x == count2:
                switch(numbers, 2, 3)
            elif x == count3:
                switch(numbers, 2, 5)
        #printGrid(numbers)

    elif emptyIndex == 3:
        numbers1 = trySwitch(temp, 3, 2)
        count1, emptyIndex = placedTiles(numbers1)

        temp = list(numbers)
        numbers2 = trySwitch(temp, 3, 6)
        count2, emptyIndex = placedTiles(numbers2)

        if lastmove == (2,3):
            switch(numbers, 3, 6)
        elif lastmove == (6,3):
            switch(numbers, 3, 2)
        else:
            x = findMin(count1, count2)
            if x== count1 and x == count2:
                a = random.choice([2,6])
                switch(numbers, 3, a)
            elif x == count1:
                switch(numbers, 3, 2)
            elif x == count2:
                switch(numbers, 3, 6)
        #printGrid(numbers)

    elif emptyIndex == 4:
        numbers1 = trySwitch(temp, 4, 1)
        count1, emptyIndex = placedTiles(numbers1)

        temp = list(numbers)
        numbers2 = trySwitch(temp, 4, 5)
        count2, emptyIndex = placedTiles(numbers2)

        temp = list(numbers)
        numbers3 = trySwitch(temp, 4, 7)
        count3, emptyIndex = placedTiles(numbers3)



        if lastmove == (1,4):
            x = findMin(count2, count3)
            if (x == count2 and x == count3):
                a = random.choice([5,7])
                switch(numbers, 4, a)
            elif x == count2:
                switch(numbers, 4, 5)
            elif x == count3:
                switch(numbers, 4, 7)
        elif lastmove == (5,4):
            x = findMin(count1, count3)
            if (x == count1 and x == count3):
                a = random.choice([1,7])
                switch(numbers, 4, a)
            elif x == count1:
                switch(numbers, 4, 1)
            elif x == count3:
                switch(numbers, 4, 7)
        elif lastmove == (7,4):
            x = findMin(count1, count2)
            if (x == count1 and x == count2):
                a = random.choice([1,5])
                switch(numbers, 4, a)
            elif x == count1:
                switch(numbers, 4, 1)
            elif x == count2:
                switch(numbers, 4, 5)
        else:
            x = findMin(count1, findMin(count2, count3))
            if x == count1 and x == count2 and x == count3:
                a = random.choice([1,5,7])
                switch(numbers, 4, a)
            elif x == count1 and x == count2:
                a = random.choice([1,5])
                switch(numbers, 4, a)
            elif x == count1 and x == count3:
                a = random.choice([1,7])
                switch(numbers, 4, a)
            elif x == count2 and x == count3:
                a = random.choice([5,7])
                switch(numbers, 4, a)
            elif x == count1:
                switch(numbers, 4, 1)
            elif x == count2:
                switch(numbers, 4, 5)
            elif x == count3:
                switch(numbers, 4, 7)
        #printGrid(numbers)

    elif emptyIndex == 5:
        numbers1 = trySwitch(temp, 5, 2)
        count1, emptyIndex = placedTiles(numbers1)

        temp = list(numbers)
        numbers2 = trySwitch(temp, 5, 4)
        count2, emptyIndex = placedTiles(numbers2)

        temp = list(numbers)
        numbers3 = trySwitch(temp, 5, 6)
        count3, emptyIndex = placedTiles(numbers3)

        temp = list(numbers)
        numbers4 = trySwitch(temp, 5, 8)
        count4, emptyIndex = placedTiles(numbers4)

        if lastmove == (2,5):
            x = findMin(count2, findMin(count3, count4))
            if(x == count2 and x == count3 and x == count4):
                a = random.choice([4,6,8])
                switch(numbers, 5, a)
            elif (x == count2 and x == count3):
                a = random.choice([4,6])
                switch(numbers, 5, a)
            elif (x == count2 and x == count4):
                a = random.choice([4,8])
                switch(numbers, 5, a)
            elif (x == count3 and x == count4):
                a = random.choice([6,8])
                switch(numbers, 5, a)
            elif x == count2:
                switch(numbers, 5, 4)
            elif x == count3:
                switch(numbers, 5, 6)
            elif x == count4:
                switch(numbers, 5, 8)
        elif lastmove == (4,5):
            x = findMin(count1, findMin(count3, count4))
            if (x == count1 and x == count3 and x == count4):
                a = random.choice([2,6,8])
                switch(numbers, 5, a)
            elif (x == count1 and x == count3):
                a = random.choice([2,6])
                switch(numbers, 5, a)
            elif (x == count1 and x == count4):
                a = random.choice([2,8])
                switch(numbers, 5, a)
            elif (x == count3 and x == count4):
                a = random.choice([6,8])
                switch(numbers, 5, a)
            elif x == count1:
                switch(numbers, 5, 2)
            elif x == count3:
                switch(numbers, 5, 6)
            elif x == count4:
                switch(numbers, 5, 8)
        elif lastmove == (6,5):
            x = findMin(count1, findMin(count2, count4))
            if (x == count1 and x == count2 and x == count4):
                a = random.choice([2,4,8])
                switch(numbers, 5, a)
            elif (x == count1 and x == count2):
                a = random.choice([2,4])
                switch(numbers, 5, a)
            elif (x == count2 and x == count4):
                a = random.choice([4,8])
                switch(numbers, 5, a)
            elif (x == count1 and x == count4):
                a = random.choice([2,8])
                switch(numbers, 5, a)
            elif x == count2:
                switch(numbers, 5, 4)
            elif x == count1:
                switch(numbers, 5, 2)
            elif x == count4:
                switch(numbers, 5, 8)
        elif lastmove == (8,5):
            x = findMin(count1, findMin(count2, count3))
            if (x == count1 and x == count2 and x == count3):
                a = random.choice([2,4,6])
                switch(numbers, 5, a)
            elif (x == count2 and x == count3):
                a = random.choice([4,6])
                switch(numbers, 5, a)
            elif (x == count1 and x == count2):
                a = random.choice([2,4])
                switch(numbers, 5, a)
            elif (x == count1 and x == count3):
                a = random.choice([2,6])
                switch(numbers, 5, a)
            elif x == count2:
                switch(numbers, 5, 4)
            elif x == count3:
                switch(numbers, 5, 6)
            elif x == count1:
                switch(numbers, 5, 2)
        else:
            x = findMin(count1, findMin(count2, findMin(count3, count4)))
            if x == count1 and x == count2 and x == count3 and  x == count4:
                a = random.choice([2,4,6,8])
                switch(numbers, 5, a)
            elif x == count1 and x == count2 and x == count3:
                a = random.choice([2,4,6])
                switch(numbers, 5, a)
            elif x == count1 and x == count2 and  x == count4:
                a = random.choice([2,4,8])
                switch(numbers, 5, a)
            elif x == count1 and x == count3 and  x == count4:
                a = random.choice([2,6,8])
                switch(numbers, 5, a)
            elif x == count2 and x == count3 and  x == count4:
                a = random.choice([4,6,8])
                switch(numbers, 5, a)
            elif x == count1 and x == count2:
                a = random.choice([2,4])
                switch(numbers, 5, a)
            elif x == count1 and x == count3:
                a = random.choice([2,6])
                switch(numbers, 5, a)
            elif x == count1 and x == count4:
                a = random.choice([2,8])
                switch(numbers, 5, a)
            elif x == count2 and x == count3:
                a = random.choice([4,6])
                switch(numbers, 5, a)
            elif x == count2 and x == count4:
                a = random.choice([4,8])
                switch(numbers, 5, a)
            elif x == count3 and x == count4:
                a = random.choice([6,8])
                switch(numbers, 5, a)
            elif x == count1:
                switch(numbers, 5, 2)
            elif x == count2:
                switch(numbers, 5, 4)
            elif x == count3:
                switch(numbers, 5, 6)
            elif x == count4:
                switch(numbers, 5, 8)
        #printGrid(numbers)

    elif emptyIndex == 6:
        numbers1 = trySwitch(temp, 6, 3)
        count1, emptyIndex = placedTiles(numbers1)

        temp = list(numbers)
        numbers2 = trySwitch(temp, 6, 5)
        count2, emptyIndex = placedTiles(numbers2)

        temp = list(numbers)
        numbers3 = trySwitch(temp, 6, 9)
        count3, emptyIndex = placedTiles(numbers3)

        if lastmove == (3,6):
            x = findMin(count2, count3)
            if(x == count2 and x == count3):
                a = random.choice([5,9])
                switch(numbers, 6, a)
            elif x == count2:
                switch(numbers, 6, 5)
            elif x == count3:
                switch(numbers, 6, 9)
        elif lastmove == (5,6):
            x = findMin(count1, count3)
            if(x == count1 and x == count3):
                a = random.choice([3,9])
                switch(numbers, 6, a)
            elif x == count1:
                switch(numbers, 6, 3)
            elif x == count3:
                switch(numbers, 6, 9)
        elif lastmove == (9,6):
            x = findMin(count1, count2)
            if (x == count1 and x == count2):
                a = random.choice([3,5])
                switch(numbers, 6, a)
            elif x == count1:
                switch(numbers, 6, 3)
            elif x == count2:
                switch(numbers, 6, 5)
        else:
            x = findMin(count1, findMin(count2, count3))
            if x == count1 and x == count2 and x == count3:
                a = random.choice([3,5,9])
                switch(numbers, 6, a)
            elif x == count1 and x == count2:
                a = random.choice([3,5])
                switch(numbers, 6, a)
            elif x == count1 and x == count3:
                a = random.choice([3,9])
                switch(numbers, 6, a)
            elif x == count2 and x == count3:
                a = random.choice([5,9])
                switch(numbers, 6, a)
            elif x == count1:
                switch(numbers, 6, 3)
            elif x == count2:
                switch(numbers, 6, 5)
            elif x == count3:
                switch(numbers, 6, 9)
        #printGrid(numbers)

    elif emptyIndex == 7:
        numbers1 = trySwitch(temp, 7, 4)
        count1, emptyIndex = placedTiles(numbers1)

        temp = list(numbers)
        numbers2 = trySwitch(temp, 7, 8)
        count2, emptyIndex = placedTiles(numbers2)

        if lastmove == (4,7):
            switch(numbers, 7, 8)
        elif lastmove == (8,7):
            switch(numbers, 7, 4)
        else:
            x = findMin(count1, count2)
            if x == count1 and x == count2:
                a = random.choice([4,8])
                switch(numbers, 7, a)
            elif x == count1:
                switch(numbers, 7, 4)
            elif x == count2:
                switch(numbers, 7, 8)
        #printGrid(numbers)

    elif emptyIndex == 8:

        numbers1 = trySwitch(temp, 8, 5)
        count1, emptyIndex = placedTiles(numbers1)

        temp = list(numbers)
        numbers2 = trySwitch(temp, 8, 7)
        count2, emptyIndex = placedTiles(numbers2)

        temp = list(numbers)
        numbers3 = trySwitch(temp, 8, 9)
        count3, emptyIndex = placedTiles(numbers3)

        if lastmove == (5,8):
            x = findMin(count2, count3)
            if (x == count2 and x == count3):
                a = random.choice([7,9])
                switch(numbers, 8, a)
            elif x == count2:
                switch(numbers, 8, 7)
            elif x == count3:
                switch(numbers, 8, 9)
        elif lastmove == (7,8):
            x = findMin(count1, count3)
            if (x == count1 and x == count3):
                a = random.choice([5,9])
                switch(numbers, 8, a)
            elif x == count1:
                switch(numbers, 8, 5)
            elif x == count3:
                switch(numbers, 8, 9)
        elif lastmove == (9,8):
            x = findMin(count1, count2)
            if (x == count1 and x == count2):
                a = random.choice([5,7])
                switch(numbers, 8, a)
            elif x == count1:
                switch(numbers, 8, 5)
            elif x == count2:
                switch(numbers, 8, 7)
        else:
            x = findMin(count1, findMin(count2, count3))
            if x == count1 and x == count2 and x == count3:
                a = random.choice([5,7,9])
                switch(numbers, 8, a)
            elif x == count1 and x == count2:
                a = random.choice([5,7])
                switch(numbers, 8, a)
            elif x == count1 and x == count3:
                a = random.choice([5,9])
                switch(numbers, 8, a)
            elif x == count2 and x == count3:
                a = random.choice([7,9])
                switch(numbers, 8, a)
            elif x == count1:
                switch(numbers, 8, 5)
            elif x == count2:
                switch(numbers, 8, 7)
            elif x == count3:
                switch(numbers, 8, 9)
        #printGrid(numbers)

    elif emptyIndex == 9:
        numbers1 = trySwitch(temp, 9, 6)
        count1, emptyIndex = placedTiles(numbers1)

        temp = list(numbers)
        numbers2 = trySwitch(temp, 9, 8)
        count2, emptyIndex = placedTiles(numbers2)

        if lastmove == (6,9):
            switch(numbers, 9, 8)
        elif lastmove == (8,9):
            switch(numbers, 9, 6)
        else:
            x = findMin(count1, count2)
            if x == count1 and x == count2:
                a = random.choice([6,8])
                switch(numbers, 9, a)
            elif x == count1:
                switch(numbers, 9, 6)
            elif x == count2:
                switch(numbers, 9, 8)
        #printGrid(numbers)

    printGrid(numbers)
    print("-------------------")
    return numbers

def switch(nums, emptyIndex, switchIndex):
    global lastmove
    nums[emptyIndex], nums[switchIndex] = nums[switchIndex], nums[emptyIndex]
    lastmove = (emptyIndex, switchIndex)
    #print(lastmove)
    return nums

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
#puzzleNumbers = [1, 4, 2, 3, 7, 5, 6, 0, 8, 9]
#puzzleNumbers = [1, 2, 3, 6, 4, 5, 9, 0, 7, 8]
#puzzleNumbers = [1, 9, 0, 2, 3, 8, 7, 4, 5, 6] # 56 steps
def call_one_puzzle():
    global puzzleNumbers
    global emptyIndex

    createGrid(puzzleNumbers)

    print("------ start ------")
    printGrid(puzzleNumbers)
    print("-------------------")

    i = 0
    while final != puzzleNumbers:
        count, emptyIndex = placedTiles(puzzleNumbers)
        #print("count", count)
        puzzleNumbers = selectSwitch(puzzleNumbers, emptyIndex)
        i += 1
        if i>10000:
            print("...not solved in 10000 steps - trying again...")
            i = 0
            createGrid(puzzleNumbers)

            print("------ start ------")
            printGrid(puzzleNumbers)
            print("-------------------")

    print("------ final ------")
    printGrid(puzzleNumbers)
    print("-------------------")

    print("...it takes ", i, "steps")

for i in range(1,11):
    print("\n----- ##### ----- THE ", i, ". PUZZLE LOADING ----- ##### -----")
    call_one_puzzle()
