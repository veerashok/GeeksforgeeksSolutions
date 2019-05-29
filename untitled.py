#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(x1, y1, x2, y2):
    count = 0

    if x2 - x1 != 0:
        slope = (y2 - y1) / (x2 - x1)

        if x1 < x2:
            rangeX = [x for x in range(x1+1, x2)]

        else:
            rangeX = [x for x in range(x2+1, x1)]


        for i in rangeX:
            y = slope * (i - x1) + y1
            intY = int(y)
            print(y, intY)
            if y - intY == 0:
                count += 1
            

    else:

        if x1 < x2:
            rangeX = [x for x in range(x1+1, x2)]

        else:
            rangeX = [x for x in range(x2+1, x1)]

        for i in rangeX:
            y = y1
            intY = int(y)

            if y - intY == 0:
                count += 1
            

    return count

if __name__ == '__main__':
    
    t = int(input())
    r = [ ]

    for t_itr in range(t):
        x1Y1X2Y2 = input().split()

        x1 = int(x1Y1X2Y2[0])

        y1 = int(x1Y1X2Y2[1])

        x2 = int(x1Y1X2Y2[2])

        y2 = int(x1Y1X2Y2[3])

        result = solve(x1, y1, x2, y2)
        r.append(result)
    print(r)
