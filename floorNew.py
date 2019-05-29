def binarySearch(tempRightArr, x):
    l = 0 
    r = len(tempRightArr)

    if arr[0] > x:
    	return - 1


    
    while r - l > 1:
        mid = int(l + (r - l)/2)
        
        if tempRightArr[mid] <= x:
        	l = mid
        else:
        	r = mid
        	
    return l


arr = list(map(int, input().strip().split()))
x = int(input())
print(binarySearch(arr, x))