def firstRepeatingElement(arr):
	temp_array = []
	for x in arr:
		temp_array.append(x)

	arr.sort()
	a = arr[0]

	repeating_elements = []
	i = 1
	while i < len(arr):
		if arr[i] == a:
			repeating_elements.append(temp_array.index(arr[i]))
		else:
			a = arr[i]
		i += 1

	if len(repeating_elements) != 0:
		min_index = min(repeating_elements)
		#print(min_index)
		#print(temp_array)
		return min_index + 1

	return -1 


t = int(input())

for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(firstRepeatingElement(arr))
	
