#!/bin/python3

import math
import os
import random
import re
import sys

def changeToDict(listIn):
    dictOut = {}
    for charIn in listIn:
        if charIn in dictOut:
            dictOut[charIn] += 1
        else:
            dictOut[charIn] = 1
    return dictOut

def checkSubString(dictNote, dictMagazine):
    res = "NO"
    for key, value in dictNote.items():
        if key in dictMagazine:
            res = "YES"
            break
    return res
            
# Complete the twoStrings function below.
def twoStrings(s1, s2):
    dictS1 = changeToDict(list(s1))
    dictS2 = changeToDict(list(s2))
    print(dictS1)
    print(dictS2)
    res = checkSubString(dictS1, dictS2)
    print(res)
    return res

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
