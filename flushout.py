n, r = list(map(int, input().strip().split()))

for _ in range(n):
	ratings = int(input())

	if ratings >= r:
		print('Good boi')
	else:
		print('Bad boi')
