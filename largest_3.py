def largestThreeElements(arr):
	first = min(arr[0], arr[1], arr[3])
	third = max(arr[0], arr[1], arr[3])
	second = 0
	i1 = arr.index(first)
	i3 = arr.index(third)
	i = [i1, i3]
	for j in range(3):
		if not j in i:
			second = arr[j]

	for i in range(2, len(arr)):
		if arr[i] > third:
			first = second
			second = third
			third = arr[i]
		elif arr[i] > second:
			first = second
			second = arr[i]
		elif arr[i] > first:
			first = arr[i]


	print(first, second, third)

arr = list(map(int, input().split()))
largestThreeElements(arr)
