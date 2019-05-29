import math

def stoogeSort(arr, N):

	if arr[0] > arr[len(arr)-1]:
		arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]

	return stoogeSort(arr[:math.ceil((2*N)/3)+1])
	return stoogeSort(arr[1-math.ceil((2*N)/3):])
	return stoogeSort(arr[:math.ceil((2*N)/3)+1])


arr = list(map(int, input().split()))
N = len(arr)
stoogeSort(arr, N)
print(arr)
