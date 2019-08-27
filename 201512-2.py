n, m = list(map(int,input().split()))
a = []
res = []
for i in range(n):
	a.append(list(map(int,input().split())))
	res.append(a[i].copy())
for i in range(n):
	cnt = 1
	for j in range(1,m):
		if a[i][j-1] == a[i][j]:
			cnt += 1
			if cnt == 3:
				res[i][j-2], res[i][j], res[i][j-1] = 0, 0, 0
			elif cnt > 3:
				res[i][j] = 0
		else:
			cnt = 1
for j in range(m):
	cnt = 1
	for i in range(1,n):
		if a[i-1][j] == a[i][j]:
			cnt += 1
			if cnt == 3:
				res[i-2][j], res[i][j], res[i-1][j] = 0, 0, 0
			elif cnt > 3:
				res[i][j] = 0
		else:
			cnt = 1
for i in range(n):
	for j in range(m):
		print(res[i][j],end=" " if j != m-1 else "\n")