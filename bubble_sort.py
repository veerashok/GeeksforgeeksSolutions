#code
def  swap(x, y):
	temp = x
	x = y 
	y = temp

	return [x, y]

def bubbleSort(arr):
	i = 0 
	j = 0 

	for i in range(len(arr)):
	    flag = 0
	    for j in range(len(arr) - 1):
	    	if arr[j+1] < arr[j]:
	    		arr[j+1], arr[j] = swap(arr[j+1], arr[j])
	    		flag = 1
	    	j += 1

	    if flag:
	    	break
	    i += 1
	return arr

t = int(input())
for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(*bubbleSort(arr))


