n = int(input())
a = list(map(int,input().split()))
a.sort()
maxN = a[-1]
minN = a[0]
if len(a) % 2 == 1:
	mid = a[len(a) // 2]
else:
	mid = (a[len(a) // 2] + a[len(a) // 2 - 1]) / 2
res = [maxN,minN,mid]
res.sort(reverse=True)
for i in range(3):
	if abs(res[i] - int(res[i])) > 0.4:
		print("{:.1f}".format(res[i]),end=(" " if i != 2 else "\n"))
	else:
		print(int(res[i]),end=(" " if i != 2 else "\n"))