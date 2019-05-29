def uniqueElement(arr):
	i = 1
	while i < len(arr) - 2:
		if arr[i] == arr[i-1]:
			i += 2
		else:
			return arr[i-1]
t = int(input())
for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(uniqueElement(arr))
