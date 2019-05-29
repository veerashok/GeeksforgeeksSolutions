def adjacentDiffOne(arr):
	if abs(arr[0] - arr[1]) == 1:
		return arr[0]

	if abs(arr[len(arr) - 1 ] - arr[len(arr) - 2]) == 1:
		return arr[len(arr) - 1]

	for i in range(1,len(arr) - 1):
		if abs(arr[i] - arr[i-1]) == 1 and abs(arr[i] - arr[i+1]) == 1:
			return arr[i]


arr = list(map(int, input().split()))
print(adjacentDiffOne(arr))
