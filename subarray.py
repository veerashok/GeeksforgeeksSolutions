def unsortedArray(arr):
	final_output = [ ]
	i = 0

	while i < len(arr) - 1:
		if arr[i] <= arr[i+1]:
			final_output.append(0)
		else:
			final_output.append(1)
		i += 1 

	#print(final_output)
	low_index = -1
	high_index = -1
	i = 0

	while i < len(final_output):
		if final_output[i] == 1 and low_index == -1:
			low_index = i
		elif final_output[i] == 1:
			high_index = i
		i += 1 
				
	if low_index == -1:
		low_index = 0 

	if high_index < len(arr) - 1:
		high_index += 1

	if high_index == 0:
		high_index = low_index + 1
	

	#print(arr[low_index:high_index+1])

	maximum = max(arr[low_index:high_index+1])
	minimum = min(arr[low_index:high_index+1])
	
	i = low_index - 1
	s = low_index
	while i >=0:
		if arr[i] > minimum:
			s = i
		i -= 1

	i = high_index + 1 
	e = high_index
	while i < len(arr):
		if arr[i] < maximum:
			e = i
		i += 1

	print(s, e)

t = int(input())
for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	unsortedArray(arr)