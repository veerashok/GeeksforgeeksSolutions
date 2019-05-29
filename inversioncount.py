def merge(arr, l, m, r):
	mergedArray = [ ]
	i = l 
	j = m

	while(i < m and j < r):
		if arr[l]
		mergedArray.append()

def mergeSort(arr, l, r):

	while( l < r):
		m = int(l + (r - l)/2)
		mergeSort(arr, l, m)
		mergeSort(arr, m, r)
		merge(arr, l, m, r)

t = int(input())
for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))

	inversionCount(arr)
