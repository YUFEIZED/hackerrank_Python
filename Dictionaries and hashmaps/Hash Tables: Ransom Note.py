#!/bin/python3

import math
import os
import random
import re
import sys

def changeToDict(listIn):
    dictOut = {}
    for charI in listIn:
        if charI in dictOut:
            dictOut[charI] += 1
        else:
            dictOut[charI] = 1
    return dictOut

def checkDict(dictNote, dictMagazine):
    res = "Yes"
    for key, value in dictNote.items():
        if key not in dictMagazine:
            res = "No"
            break
        elif value > dictMagazine[key]:
            res = "No"
            break
    return res
            
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dictMagazine = changeToDict(magazine)
    dictNote = changeToDict(note)
    print(checkDict(dictNote, dictMagazine))

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
