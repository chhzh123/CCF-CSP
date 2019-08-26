n = int(input())
s = list(map(int,input().split()))
a = [0] * 10005
for i in range(len(s)):
	a[s[i]] = 1
res = 0
for i in range(10001):
	if a[i] == 1 and a[i+1] == 1:
		res += 1
print(res)