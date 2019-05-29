def countingSort(arr):
	count = [0] * 10
	out = [0] * len(arr)

	for x in arr:
		count[x] += 1

	for i in range(1, len(count)):
		count[i] = count[i-1] + count[i]

	for x in arr:
		out[count[x] - 1] = x
		count[x] -= 1

	for i in range(len(out)):
		arr[i] = out[i]

	print(arr)

arr = list(map(int, input().strip().split()))
countingSort(arr)
