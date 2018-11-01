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

def compareLists(dict1, s2):
    if dict1==changeToDict(s2):
        return True
    else:
        return False
    
def creatSub(size, s):
    listSub = []
    listS = list(s)
    for i in range(len(listS)-size+1):
        listTmp = []
        for j in range(i,i+size):
            listTmp.append(listS[j])
        listSub.append(listTmp)
    return listSub
    
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    dictS = changeToDict(s)
    res = 0
    for key, value in dictS.items():
        if value>1:
            res += int(value*(value-1)/2)   
    for size in range(2, len(list(s))):
        listSub = creatSub(size, s)
        for i in range(len(listSub)):
            dict1 = changeToDict(listSub[i])
            for j in range(i+1, len(listSub)):
                if compareLists(dict1, listSub[j]) == True:
                    res += 1
    return res                     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
