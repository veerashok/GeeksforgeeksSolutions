def allSubStrs(str):
	count = 0
	i = 0
	substr = '010'

	updatedStr = ''
	instanceIndices = [ ]

	while i < len(str):
		try:
			j = str.index(substr, i)
			instanceIndices.append(j)
			i = int(j+1)
		except:
			i += 1

	for x in instanceIndices:
		if x + 3 < len(str):
			updatedStr = updatedStr + str[x:x+2] + '1'
			count += 1 

	print(count)

n = input()
str = input()
allSubStrs(str)