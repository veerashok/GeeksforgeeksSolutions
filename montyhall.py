import random
s = set([1, 2, 3])
x = random.randint(1, 3)
print(x)
y = int(input())
s1 = set([x, y])
print(*list(s - s1))


