def peakelement(arr):
	if arr[0] >= arr[1]:
		return 0

	i = 1 
	while i < len(arr) - 1:
		if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
			return i 
		else:
			i += 1  

	if arr[len(arr) - 1] >= arr[len(arr) - 2]:
		return len(arr) - 1 

t = int(input())
outputList = []
for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	outputList.append(peakelement(arr))
print(*outputList)



