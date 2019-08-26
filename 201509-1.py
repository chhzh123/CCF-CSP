n = input()
a = list(map(int,input().split()))
a += [-1]
res = 0
for i in range(len(a)-1):
	if a[i] != a[i+1]:
		res += 1
print(res)