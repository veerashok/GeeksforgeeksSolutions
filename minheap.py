import math

def swap(x, y):
	temp = x
	x = y 
	y = temp
	return [x, y]

def deletion(arr, p):
	size = len(arr)
	arr[size - 1], arr[p] = swap(arr[size - 1], arr[p])
	parent = p
	arr = arr[:size - 1]

	left_child = 2 * parent + 2

	right_child = 2 * parent + 1

	while right_child <= len(arr) - 1 and left_child <= len(arr) - 1 :

		if left_child <= len(arr) - 1 and (arr[parent] > arr[left_child] or arr[parent] > arr[right_child]):
			if arr[left_child] > arr[right_child]:
				arr[right_child], arr[parent] = swap(arr[right_child], arr[parent])
				parent = right_child
			else:
				arr[left_child], arr[parent] = swap(arr[left_child], arr[parent])
				parent = left_child
		elif right_child <= len(arr) - 1 and arr[parent] > arr[right_child]:
			arr[right_child], arr[parent] = swap(arr[right_child], arr[parent])
			parent = right_child

		left_child = 2 * parent + 2
		right_child = 2 * parent + 1
		print(left_child)
		print(right_child)

	return arr

def insertion(arr, x):
	arr.append(x)

	child = len(arr) - 1

	parent = math.ceil(child / 2) - 1

	while parent >= 0:
		if arr[parent] > arr[child]:
			arr[parent], arr[child] = swap(arr[parent], arr[child])
		child = parent
		parent = math.ceil(child / 2) - 1

	return arr


def heapify(arr):

	root = 0 
	parent = 0 
	size = len(arr)

	f_l = int( size / 2 )

	for i in range(f_l, size):
		child = i
		parent = math.ceil(child / 2) - 1
		while parent >= 0 :
			if arr[parent] > arr[child]:
				arr[parent], arr[child] = swap(arr[parent], arr[child])
			child = parent
			parent = math.ceil(child / 2) - 1

	return arr

t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr = heapify(arr)
    for j in range(len(arr) - k):
        arr = deletion(arr, 0)
    print(*arr)









