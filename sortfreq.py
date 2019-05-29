def sortbyFreq(arr):
	maximum = max(arr)
	count = [0]*(maximum+1)

	final_output = [ ]

	for x in arr:
		count[x] += 1

	
	max_count = max(count)

	while max_count != 0:

		max_index = count.index(max_count)

		for _ in range(max_count):
			final_output.append(max_index)

		count[max_index] = 0
		max_count = max(count)

	print(*final_output)

	


t = int(input())
for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	sortbyFreq(arr)
