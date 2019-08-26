r, y, g = list(map(int,input().split()))
n = int(input())
res = 0
for i in range(n):
	k, t = list(map(int,input().split()))
	tmp = res
	if k == 3:
		continue
	elif k == 2:
		res += t + r
	elif k == 1:
		res += t
	else:
		res += t
print(res)