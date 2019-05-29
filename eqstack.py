#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    l1 = sum(h1)
    l2 = sum(h2)
    l3 = sum(h3)
    i = 0
    j = 0
    k = 0

    while l1 != l2 or l1 != l3 or l2 != l3:
        flag = 0
        if l1 > l2 and l1 > l3:
            i += 1
            flag = 1
        
        elif l2 > l1 and l2 > l3:
            j += 1
            flag = 1
        
        elif l3 > l1 and l3 > l2:
            k += 1
            flag = 1
        
        if l1 == l2 and l1 > l3 and flag == 0:
            if h1[i] > h2[j]:
                i += 1
            elif h1[i] == h2[j]:
                i += 1 
                j += 1
            else:
                j += 1 
        
        elif l1 == l3 and l3 > l2 and flag ==0:
            if h1[i] > h3[k]:
                i += 1
            elif h1[i] == h3[k]:
                i += 1 
                k += 1
            else:
                k += 1 

        elif l2 == l3 and l3 > l1 and flag == 0:
            if h2[j] > h3[k]:
                j += 1
            elif h2[j] == h3[k]:
                j += 1 
                k += 1
            else:
                k += 1

        # print(h1[i:], i)
        # print(h2[j:], j)
        # print(h3[k:], k)


        l1 = sum(h1[i:])
        l2 = sum(h2[j:])
        l3 = sum(h3[k:])

        if l1 == 0:
            return 0
        
        if l2 == 0:
            return 0
        
        if l3 == 0:
            return 0

        if i >= len(h1) or j >= len(h2) or k >= len(h3):
            break

        
    return l1

if __name__ == '__main__':

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(result)

