def getKey(item):
	return item[1]

def maxDiffFreq(arr):
	distElements = sorted(list(set(arr)))

	out = [ ]
	for x in distElements:
		out.append([x, arr.count(x)])

	out.sort(key=getKey)

	print(out)



arr = list(map(int, input().strip().split()))
maxDiffFreq(arr)
