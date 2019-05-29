  def magic(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s

def largestEvenNum(num):
	numList = [int(x) for x in list(num)]
	#print(numList)
	numList.sort()
	numList.reverse()
	
	i = len(numList) - 1

	even_digit = -1 
	even_index = -1

	while i >= 0:
		if numList[i] % 2 == 0:
			even_digit = numList[i]
			even_index = i
			break 
		i -= 1

	if even_index != -1:
		del numList[even_index]
		numList.append(even_digit)
		print(magic(numList))
	else:
		print(magic(numList))





t = int(input())
for _ in range(t):
	largestEvenNum(input())
