def floor(arr, x):
	l = 0
	r = len(arr) - 1

	while r - l > 1:
		m = int(l + ( r - l ) / 2)
		if arr[m] == x:
			return m

		if arr[m] <= x:
			l = m 
		else:
			r = m 

	return l

def kclosestelements(arr, x, k):
	outputElements = [ ]
	index = floor(arr, x)
	d = int(k / 2)

	if arr[index] == x:
		if index - d >= 0 and index + d < len(arr):
			for j in range(index - d, index):
				outputElements.append(arr[j])

			for j in range(index + 1, index + d + 1):
				outputElements.append(arr[j])

	
		elif index - d >= 0:
			m = len(arr) - 1 - index
			l = k - m 
			for j in range(index - l, index):
				outputElements.append(arr[j])

			if m > 0:
				for j in range(index + 1, index + m + 1):
					outputElements.append(arr[j])

		else:
			m = index - 1
			l = k - m 
			for j in range(index):
				outputElements.append(arr[j])

			for j in range(index + 1, index + l + 1):
				outputElements.append(arr[j])

	else:
		if index - d >= 0 and index + d < len(arr):
			for j in range(index - d, index+1):
				outputElements.append(arr[j])

			for j in range(index + 1, index + d + 1):
				outputElements.append(arr[j])

	
		elif index - d >= 0:
			m = len(arr) - 1 - index
			l = k - m 
			for j in range(index - l, index+1):
				outputElements.append(arr[j])

			for j in range(index + 1, index + m + 1):
				outputElements.append(arr[j])

		else:
			m = index - 1
			l = k - m 
			for j in range(index+1):
				outputElements.append(arr[j])

			for j in range(index + 1, index + l + 1):
				outputElements.append(arr[j])


	return outputElements






t = int(input())
for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	k, x = list(map(int, input().split()))
	print(*kclosestelements(arr,x,k))
