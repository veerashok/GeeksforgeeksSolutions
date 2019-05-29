#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    seqList = [ ]
    

    for i in range(n):
        tempList = []
        seqList.append(tempList)
        
    lastAnswer = 0
    
    for x in queries:
        if x[0] == 1:
            i = (x[1] ^ lastAnswer) % n
            seq = seqList[i]
            seq.append(x[2])
            seqList[i] = seq

        
        if x[0] == 2:
            i = (x[1] ^ lastAnswer) % n
            seq = seqList[i]
            lastAnswer = seq[len(seq) - 1]

    for x in seqList:
        print(x)
            
            
        
if __name__ == '__main__':

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)