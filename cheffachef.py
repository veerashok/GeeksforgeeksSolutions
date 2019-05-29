t = int(input())
for _ in range(t):
	n = int(input())
	out = [2] + [0]*n
	print(1, 1, 1, 1)
	out[1] = int(input())
	for i in range(2, n+1):
		print(1, i, i, i)
		out[i] = int(input())
	print(*out)
	int(input())


