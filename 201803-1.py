a = list(map(int,input().split()))
res = 0
tmp = 0
for i in range(len(a)):
	if a[i] == 1:
		res += 1
		tmp = 0
	elif a[i] == 0:
		break
	else:
		tmp += 2
		res += tmp
print(res)