#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def isBeautiful(s, i, isNine):
    numArr = [ ]
    if isNine == 0:
        for j in range(0, len(s), i):
            #print(int(s[j:j+i]))
            numArr.append(int(s[j:j+1]))
    else:
        numArr.append(int(s[:i]))

        for j in range(i, len(s), i+1):
            #print(int(s[j:j+i]))
            numArr.append(int(s[j:j+i+1]))

    flag = 1
    i = 1
    while i < len(numArr):
        if numArr[i] - numArr[i-1] != 1:
            flag == 0
        i +=1 

    if flag == 0:
        print("NO")
    else:
        print("YES" + " " + str(numArr[0]))



def separateNumbers(s):
    isNine = 0
    flag = 0
    for i in range(1, int(len(s)/2)):
        flag = 1
        num1 = int(s[:i])
        num2 = int(s[i:i+1])
        num3 = int(s[i:i+2])
        
        if num1 + 1 == num2:
            isBeautiful(s, i, isNine);
            break
        
        if num1 + 1 == num3:
            isNine = 1
            isBeautiful(s, i, isNine)
            break
    
    if flag == 0:
        print("NO")
        
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
