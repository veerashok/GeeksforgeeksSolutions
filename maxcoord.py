#!/bin/python3

import os
import sys
import math

# Complete the solve function below.
def getKeyX(item):
    return item[0]

def getKeyY(item):
    return item[1]

def solve(coordinates):
    
    xaxisCords = []
    yaxisCords = []
    
    for x in coordinates:
        if x[0] == 0:
            yaxisCords.append(x)
        else:
            xaxisCords.append(x)
            
    xaxisCords = sorted(xaxisCords, key=getKeyX)
    yaxisCords = sorted(yaxisCords, key=getKeyY)
    
    x11 = xaxisCords[0][0]
    x12 = xaxisCords[len(xaxisCords) -1][0]
    
    y21 = yaxisCords[0][1]
    y22 = yaxisCords[len(yaxisCords) - 1][1]
    
    dist = max(y22-y21, x12-x12)
    
    dist1 = math.sqrt(pow(x12, 2) + pow(y21, 2))
    
    dist2 = math.sqrt(pow(x11, 2) + pow(y21, 2))
    
    dist3 = math.sqrt(pow(x11, 2) + pow(y22, 2))
    
    dist4 = math.sqrt(pow(x12, 2) + pow(y22, 2))
    
    
    

    return max([dist, dist1, dist2, dist3, dist4])

if __name__ == '__main__':

    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)
    print(result)
    