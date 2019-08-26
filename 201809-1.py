n = int(input())
a = list(map(int,input().split()))
res = [0] * n
for i in range(n):
	if i == 0:
		res[i] = (a[i] + a[i+1]) // 2
	elif i == n-1:
		res[i] = (a[i-1] + a[i]) // 2
	else:
		res[i] = (a[i] + a[i+1] + a[i-1]) // 3
for i in range(n):
	print(res[i],end=(" " if i != n-1 else "\n"))