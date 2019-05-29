import math

def merge(arr1, arr2):
	merged_array = [ ]

	i = 0 
	j = 0 
	while i < len(arr1) and j < len(arr2):

		if arr1[i] > arr2[j]:
			merged_array.append(arr2[j])
			j += 1
		else:
			merged_array.append(arr1[i])
			i += 1

	while i < len(arr1):
		merged_array.append(arr1[i])
		i += 1 


	while j < len(arr2):
		merged_array.append(arr2[j])
		j += 1 


	return merged_array


def insertionSort(a):

	for i in range(1, len(a)):
		index = 0
		for j in range(i+1):
			if a[i] > a[j]:
				index += 1

		a.insert(index, a[i])
		del a[i+1]
	return a

def timSort(arr):
	output_arr = [ ]
	run = 32

	iteration = int(len(arr) / 32)

	for j in range(iteration):
		output_arr.append(insertionSort(arr[j*run:(j+1)*run]))


	output_arr.append(insertionSort(arr[run*iteration:]))


	final_output = [ ]

	if len(output_arr) == 1:
		final_output = output_arr[0]
		return final_output
	
	i = 1
	while(i < len(output_arr)):
		merged_arr = merge(output_arr[i-1], output_arr[i])

		for x in merged_arr:
			final_output.append(x)

	return final_output


arr = list(map(int, input().split()))
print(*timSort(arr))





