n, k = list(map(int,input().split()))
a = list(map(int,input().split()))
res = 0
tmp = 0
for i in range(n):
	tmp += a[i]
	if tmp >= k:
		res += 1
		tmp = 0
if tmp != 0:
	res += 1
print(res)