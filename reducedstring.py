#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(L):
    L = list(L)
    
    while(len(L) != len(set(L))):
        i = 0
        prev = L
        while i < len(L) - 1:
            if L[i] == L[i+1]:
                del L[i]
                del L[i]
                break
            i += 1
        current = L
        if prev == current:
            break
    if len(L) == 0:
        return "Empty String"
    else:
        return ''.join(L)

if __name__ == '__main__':

    s = input()

    result = superReducedString(s)

    print(result)


    