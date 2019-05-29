def posNegR(arr):

	low = 0
	mid = 0 
	high = len(arr) - 1

	while low <= high:

		if arr[mid] < 0:
			#swap mid and low
			arr[mid], arr[low] = arr[low], arr[mid]
			low += 1
			mid += 1
		elif arr[mid] == 0:
			mid += 1
		elif arr[mid] > 0:
			# Swap mid and high
			arr[high], arr[mid] = arr[mid], arr[high]
			high -= 1

arr = list(map(int, input().split()))
posNegR(arr)
print(arr)