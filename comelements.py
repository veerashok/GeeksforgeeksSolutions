def commonElements(A, B, C):
	commonArray = []

	i = 0
	j = 0 
	k = 0 

	while(i < len(A) and j < len(C) and k < len(C)):
		if A[i] == B[j] and B[j] == C[k]:
			commonArray.append(A[i])
			i += 1
			j += 1
			k += 1
		else:
			if A[i] <= B[j] and A[i] <= C[k]:
				i += 1 

			elif B[j] <= A[i] and B[j] <= C[k]:
				j += 1

			elif C[k] <= A[i]  and C[k] <= B[j]:
				k += 1
	
	return commonArray





t = int(input())

for i in range(t):
	n1, n2, n3 = list(map(int, input().split()))
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	C = list(map(int, input().split()))
	commonArray = commonElements(A, B, C)
	if len(commonArray) == 0:
		print(-1)
	else:
		print(commonArray)