#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def getKey(item):
    return item[1]

def getKey2(item):
    return item[0]

def bigSorting(unsorted):
    final_out = [ ]
    output = [ ]
    for x in unsorted:
        temp = [int(x), len(x)]
        output.append(temp)
    output = sorted(output, key=getKey)
    
    tempSizes = [ ]
    for x in output:
        tempSizes.append(x[1])
    
    i = 0 
    temp_arr = [ ]
    j = 0
    while i < len(output):
        if len(temp_arr) == 0:
            temp_arr.append(output[i])
        elif temp_arr[j-1][1] == output[i][1]:
            temp_arr.append(output[i])
            j += 1
        else:
            temp_arr = sorted(temp_arr, key=getKey2)
            for x in temp_arr:
                final_out.append(str(x[0]))
            temp_arr = [ ]
            temp_arr.append(output[i])
            j = 0
        
        i += 1
    final_out.append(str(temp_arr[0][0]))   
    
    return final_out
        
if __name__ == '__main__':

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)
    
    print(result)
