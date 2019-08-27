n, k = list(map(int,input().split()))
a = [i for i in range(1,n+1)]
cnt = 1
i = 0
while len(a) > 1:
	if cnt % k == 0 or cnt % 10 == k:
		a = a[:i] + a[i+1:]
		i -= 1
	i += 1
	cnt += 1
	if i >= len(a):
		i = 0
print(a[0])