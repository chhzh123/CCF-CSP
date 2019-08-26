n = int(input())
a = list(map(int,input().split()))
a.sort()
res = 0x3f3f3f3f
for i in range(n-1):
	res = min(res,abs(a[i] - a[i+1]))
print(res)