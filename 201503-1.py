n, m = map(int,input().split())
a = []
for i in range(n):
	a.append(list(map(int,input().split())))
for i in range(m):
	for j in range(n):
		print(a[j][-i-1],end=(" " if j != n-1 else "\n"))