def floor(arr, x):
	l = 0
	r = len(arr) - 1

	if arr[l] > x:
		return -1


	while(r - l > 1):
		m = int(l + ( r - l ) / 2)
		if arr[m] <= x:
			l = m 
		else:
			r = m 

	return l

t = int(input())
for i in range(t):
	n, x = list(map(int, input().split()))
	arr = list(map(int, input().split()))
	print(floor(arr, x))
