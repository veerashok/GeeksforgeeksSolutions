def countingSort(arr):
	maximum = max(arr)

	output = [0] * (len(arr))
	count = [0] * (maximum + 1)

	for x in arr:
		count[x] += 1

	sortedArray = [ ]

	i = 1
	while(i < len(count)):
		count[i] += count[i-1]
		i += 1

	for x in arr:
		output[count[x] - 1] = x
		count[x] -= 1
	print(*output)


arr = list(map(int, input().split()))
countingSort(arr)



