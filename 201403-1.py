n = int(input())
a = list(map(int,input().split()))
cnt = [0] * 2005
for i in range(n):
	cnt[a[i]] += 1
res = 0
for i in range(1001):
	if cnt[i] == 1 and cnt[-i] == 1:
		res += 1
print(res)