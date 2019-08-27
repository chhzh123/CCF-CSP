n = int(input())
a = list(map(int,input().split()))
res = {}
for i in range(n):
	res[a[i]] = res.get(a[i],0) + 1
res = res.items()
res = sorted(res,key=lambda x: (x[1],-x[0]),reverse=True)
for i in range(len(res)):
	print(res[i][0],res[i][1])