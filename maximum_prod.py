def max_prod(arr):
	first_pos = min(arr[0], arr[1])
	second_pos = max(arr[0], arr[1])

	first_neg = abs(min(arr[0], arr[1]))
	second_neg = abs(max(arr[0], arr[1]))

	i = 2

	while(i < len(arr)):
		if arr[i] < 0:
			if abs(arr[i]) > abs(second_neg):
				first_neg = second_neg
				second_neg = abs(arr[i])
			elif abs(arr[i]) > abs(first_neg):
				first_neg = abs(arr[i])
		else:
			if arr[i] > second_pos:
				first_pos = second_pos
				second_pos = arr[i]
			elif arr[i] > first_pos:
				first_pos = arr[i]
		i += 1 

	print(first_pos, second_pos)

	return max(first_pos*second_pos, first_neg*second_neg)


arr = list(map(int, input().split()))
print(max_prod(arr))

