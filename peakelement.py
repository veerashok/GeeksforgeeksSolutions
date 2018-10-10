def peakelement(arr):

	if arr[0] >= arr[1]:
		return 0

	i = 1 
	while i < len(arr) - 1:
		if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
			return i 

	if arr[len(arr) - 1] >= ar[len(arr) - 2]:
		return len(arr) - 1 

t = int(input())

for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(peakelement)



