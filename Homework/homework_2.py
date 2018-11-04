#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:51:03 2018

@author: caggri
"""
import random
puzzleNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
final = list(puzzleNumbers)
grid = [[], [], [], []]
lastmove = (0,1)

def createGrid(puzzleNumbers):
    while puzzleNumbers[0] != 1:
        random.shuffle(puzzleNumbers)
    tmp = list(puzzleNumbers)  # creates a temporary lisy from shuffled list
    tmp.remove(0)  # removes the 0
    count = checkSolvable(tmp)
    shuffle_status(count)
    return puzzleNumbers

def checkSolvable(arr):
    count = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if arr[i] > arr[j]:
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
    count = 0
    i=9
    while nums[i] == i and i>=0:
        count += 1
        i -= 1
    for i in range(0,10):
        if nums[i] == 0:
            emptyIndex = i
    return count, emptyIndex

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

        y = findMax(count2,count3)

        if count1 == 10:
            switch(numbers, 1, 0)
        elif lastmove == (2,1):
            switch(numbers, 1, 4)
        elif lastmove == (4,1):
            switch(numbers, 1, 2)
        else:
            if y == count2 and y == count3:
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

        x = findMax(count1, findMax(count2, count3))

        if lastmove == (1,2):
            if x == count1 or (x == count2 and x == count3):
                a = random.choice([3,5])
                switch(numbers, 2, a)
            elif x == count1 or x == count2:
                switch(numbers, 2, 3)
            elif x == count1 or x == count3:
                switch(numbers, 2, 5)
        elif lastmove == (3,2):
            if x == count2 or (x == count1 and x == count3):
                a = random.choice([1,5])
                switch(numbers, 2, a)
            elif x == count2 or x == count1:
                switch(numbers, 2, 1)
            elif x == count2 or x == count3:
                switch(numbers, 2, 5)
        elif lastmove == (5,2):
            if x == count3 or (x == count1 and x == count2):
                a = random.choice([1,3])
                switch(numbers, 2, a)
            elif x == count3 or x == count1:
                switch(numbers, 2, 1)
            elif x == count3 or x == count2:
                switch(numbers, 2, 3)
        else:
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

        x = findMax(count1, count2)

        if lastmove == (2,3):
            switch(numbers, 3, 6)
        elif lastmove == (6,3):
            switch(numbers, 3, 2)
        else:
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

        x = findMax(count1, findMax(count2, count3))

        if lastmove == (1,4):
            if x == count1 or (x == count2 and x == count3):
                a = random.choice([5,7])
                switch(numbers, 4, a)
            elif x == count1 or x == count2:
                switch(numbers, 4, 5)
            elif x == count1 or x == count3:
                switch(numbers, 4, 7)
        elif lastmove == (5,4):
            if x == count2 or (x == count1 and x == count3):
                a = random.choice([1,7])
                switch(numbers, 4, a)
            elif x == count2 or x == count1:
                switch(numbers, 4, 1)
            elif x == count2 or x == count3:
                switch(numbers, 4, 7)
        elif lastmove == (7,4):
            if x == count3 or (x == count1 and x == count2):
                a = random.choice([1,5])
                switch(numbers, 4, a)
            elif x == count3 or x == count1:
                switch(numbers, 4, 1)
            elif x == count3 or x == count2:
                switch(numbers, 4, 5)
        else:
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

        x = findMax(count1, findMax(count2, findMax(count3, count4)))

        if lastmove == (2,5):
            if x == count1 or (x == count2 and x == count3 and x == count4):
                a = random.choice([4,6,8])
                switch(numbers, 5, a)
            elif x == count1 or (x == count2 and x == count3):
                a = random.choice([4,6])
                switch(numbers, 5, a)
            elif x == count1 or (x == count2 and x == count4):
                a = random.choice([4,8])
                switch(numbers, 5, a)
            elif x == count1 or (x == count3 and x == count4):
                a = random.choice([6,8])
                switch(numbers, 5, a)
            elif x == count1 or x == count2:
                switch(numbers, 5, 4)
            elif x == count1 or x == count3:
                switch(numbers, 5, 6)
            elif x == count1 or x == count4:
                switch(numbers, 5, 8)
        elif lastmove == (4,5):
            if x == count2 or (x == count1 and x == count3 and x == count4):
                a = random.choice([2,6,8])
                switch(numbers, 5, a)
            elif x == count2 or (x == count1 and x == count3):
                a = random.choice([2,6])
                switch(numbers, 5, a)
            elif x == count2 or (x == count1 and x == count4):
                a = random.choice([2,8])
                switch(numbers, 5, a)
            elif x == count2 or (x == count3 and x == count4):
                a = random.choice([6,8])
                switch(numbers, 5, a)
            elif x == count2 or x == count1:
                switch(numbers, 5, 2)
            elif x == count2 or x == count3:
                switch(numbers, 5, 6)
            elif x == count2 or x == count4:
                switch(numbers, 5, 8)
        elif lastmove == (6,5):
            if x == count3 or (x == count1 and x == count2 and x == count4):
                a = random.choice([2,4,8])
                switch(numbers, 5, a)
            elif x == count3 or (x == count1 and x == count2):
                a = random.choice([2,4])
                switch(numbers, 5, a)
            elif x == count3 or (x == count2 and x == count4):
                a = random.choice([4,8])
                switch(numbers, 5, a)
            elif x == count3 or (x == count1 and x == count4):
                a = random.choice([2,8])
                switch(numbers, 5, a)
            elif x == count3 or x == count2:
                switch(numbers, 5, 4)
            elif x == count3 or x == count1:
                switch(numbers, 5, 2)
            elif x == count3 or x == count4:
                switch(numbers, 5, 8)
        elif lastmove == (8,5):
            if x == count4 or (x == count1 and x == count2 and x == count3):
                a = random.choice([2,4,6])
                switch(numbers, 5, a)
            elif x == count4 or (x == count2 and x == count3):
                a = random.choice([4,6])
                switch(numbers, 5, a)
            elif x == count4 or (x == count1 and x == count2):
                a = random.choice([2,4])
                switch(numbers, 5, a)
            elif x == count4 or (x == count1 and x == count3):
                a = random.choice([2,6])
                switch(numbers, 5, a)
            elif x == count4 or x == count2:
                switch(numbers, 5, 4)
            elif x == count4 or x == count3:
                switch(numbers, 5, 6)
            elif x == count4 or x == count1:
                switch(numbers, 5, 2)
        else:
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

        x = findMax(count1, findMax(count2, count3))

        if lastmove == (3,6):
            if x == count1 or (x == count2 and x == count3):
                a = random.choice([5,9])
                switch(numbers, 6, a)
            elif x == count1 or x == count2:
                switch(numbers, 6, 5)
            elif x == count1 or x == count3:
                switch(numbers, 6, 9)
        elif lastmove == (5,6):
            if x == count2 or (x == count1 and x == count3):
                a = random.choice([3,9])
                switch(numbers, 6, a)
            elif x == count2 or x == count1:
                switch(numbers, 6, 3)
            elif x == count2 or x == count3:
                switch(numbers, 6, 9)
        elif lastmove == (9,6):
            if x == count3 or (x == count1 and x == count2):
                a = random.choice([3,5])
                switch(numbers, 6, a)
            elif x == count3 or x == count1:
                switch(numbers, 6, 3)
            elif x == count3 or x == count2:
                switch(numbers, 6, 5)
        else:
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

        x = findMax(count1, count2)

        if lastmove == (4,7):
            switch(numbers, 7, 8)
        elif lastmove == (8,7):
            switch(numbers, 7, 4)
        else:
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

        x = findMax(count1, findMax(count2, count3))

        if lastmove == (5,8):
            if x == count1 or (x == count2 and x == count3):
                a = random.choice([7,9])
                switch(numbers, 8, a)
            elif x == count1 or x == count2:
                switch(numbers, 8, 7)
            elif x == count1 or x == count3:
                switch(numbers, 8, 9)
        elif lastmove == (7,8):
            if x == count2 or (x == count1 and x == count3):
                a = random.choice([5,9])
                switch(numbers, 8, a)
            elif x == count2 or x == count1:
                switch(numbers, 8, 5)
            elif x == count2 or x == count3:
                switch(numbers, 8, 9)
        elif lastmove == (9,8):
            if x == count3 or (x == count1 and x == count2):
                a = random.choice([5,7])
                switch(numbers, 8, a)
            elif x == count3 or x == count1:
                switch(numbers, 8, 5)
            elif x == count3 or x == count2:
                switch(numbers, 8, 7)
        else:
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

        x = findMax(count1, count2)

        if lastmove == (6,9):
            switch(numbers, 9, 8)
        elif lastmove == (8,9):
            switch(numbers, 9, 6)
        else:
            if x == count1 and x == count2:
                a = random.choice([6,8])
                switch(numbers, 9, a)
            elif x == count1:
                switch(numbers, 9, 6)
            elif x == count2:
                switch(numbers, 9, 8)
        #printGrid(numbers)

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

def findMax(a, b):
    min = 0
    if a <= b:
        return b
    else:
        return a

""" main """
#puzzleNumbers = [1, 4, 2, 3, 7, 5, 6, 0, 8, 9]
#puzzleNumbers = [1, 2, 3, 6, 4, 5, 9, 0, 7, 8]
#puzzleNumbers = [1, 4, 5, 2, 7, 0, 3, 6, 8, 9]
def call_one_puzzle():
    global puzzleNumbers
    global emptyIndex

    createGrid(puzzleNumbers)

    print("--- start ---")
    printGrid(puzzleNumbers)
    print("-------------")

    i = 0
    while final != puzzleNumbers:
        misplacedTileNo, emptyIndex = placedTiles(puzzleNumbers)
        #print("emptyIndex", emptyIndex)
        puzzleNumbers = selectSwitch(puzzleNumbers, emptyIndex)
        i += 1
        if i>100000:
            print("...not solved in 100000 steps - trying again...")
            i = 0
            createGrid(puzzleNumbers)

            print("--- start ---")
            printGrid(puzzleNumbers)
            print("-------------")

    print("--- final ---")
    printGrid(puzzleNumbers)
    print("-------------")

    print("...it takes ", i, "steps")


for i in range(1,11):
    print("\n----- ##### ----- THE ", i, ". PUZZLE LOADING ----- ##### -----")
    call_one_puzzle()
