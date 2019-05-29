def getKey(item):
	return item[0]

def permuteLeft(arr):
	temp = sorted(arr)
	op1 = [ ]
	op2 = [ ]

	for key, value in enumerate(arr):
		op1.append([value,key])

	for key, value in enumerate(temp):
		op2.append([value,key])

	op1.sort(key=getKey)

	i = 0
	diffs = [ ]
	while i < len(op2):
		diffs.append(op1[i][1] - op2[i][1])
		i += 1

	print(diffs)

arr = list(map(int, input().strip().split()))
permuteLeft(arr)