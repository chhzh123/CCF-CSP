n = int(input())
a = list(map(int,input().split()))
cnt = [0] * 1005
for i in range(len(a)):
	cnt[a[i]] += 1
sumup = 0
b = max(a)
flag = False
for i in range(b+1):
	if cnt[i] != 0:
		if sumup == n - cnt[i] - sumup:
			print(i)
			flag = True
			break
		else:
			sumup += cnt[i]
if not flag:
	print("-1")