def insertionSort(arr):

	for i in range(1, len(arr)):
		index = 0
		for j in range(i+1):
			if arr[i] > arr[j]:
				index += 1

		arr.insert(index, arr[i])
		del arr[i+1]
		
	print(*arr)

t = int(input())
for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	insertionSort(arr)

