#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):

    if a < b:

        output = [ ]
        
        total = n - 1
        
        i = total
        while i >= 0:
            output.append((i * a) + (total - i) * b)
            i = i - 1

        return output

    else:

        output = [ ]
        
        total = n - 1
        
        i = total
        while i >= 0:
            output.append((i * b) + (total - i) * a)
            i = i - 1

        return output

    

if __name__ == '__main__':
   
    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        print(*result)
