def DNF(a, lowVal, highVal):
	print(lowVal, highVal)
	low = 0
	high = len(arr) - 1
	mid = 0

	while mid <= high:
		if a[mid] <= lowVal:
			a[low], a[mid] = a[mid], a[low]
			mid += 1 
			low += 1
		elif a[mid] > lowVal and a[mid] <= highVal:
			mid += 1
		elif a[mid] >= highVal:
			a[high], a[mid] = a[mid], a[high]
			high -= 1
	print(a)

t = int(input())
for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	a1 = list(map(int, input().split()))
	lowVal = a1[0]
	highVal = a1[1]
	DNF(arr, lowVal, highVal)
