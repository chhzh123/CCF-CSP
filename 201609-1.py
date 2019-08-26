n = int(input())
a = list(map(int,input().split()))
res = 0
for i in range(len(a)-1):
	res = max(res,abs(a[i+1] - a[i]))
print(res)