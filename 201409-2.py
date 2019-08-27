n = int(input())
a = []
for i in range(101):
	a.append([0]*101)
for i in range(n):
	x1, y1, x2, y2 = list(map(int,input().split()))
	for i in range(x1,x2):
		for j in range(y1,y2):
			a[i][j] = 1
res = 0
for i in range(101):
	for j in range(101):
		if a[i][j] == 1:
			res += 1
print(res)