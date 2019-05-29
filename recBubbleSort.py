def  swap(x, y):
	temp = x
	x = y 
	y = temp

	return [x, y]

def recBubbleSort(arr, n):

	if n > 0:
		for i in range(n-1):
			if arr[i] > arr[i+1]:
				arr[i+1], arr[i] = swap(arr[i+1], arr[i])

		return recBubbleSort(arr, n-1)

	else:
		return arr

arr = list(map(int, input().split()))
print(*recBubbleSort(arr, len(arr)))

