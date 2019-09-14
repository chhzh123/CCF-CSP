n = int(input())
hArr = list(map(int,input().split()))
maxArea = 0
maxH = max(hArr)
for h in range(1, maxH+1):
	a, b = -1, -1
	flag = False
	for i in range(n + 1):
		if i != n and hArr[i] >= h:
			if not flag:
				a = i
				flag = True
			else:
				pass
		else:
			b = i
			if a != -1:
				maxArea = max(maxArea, (b - a) * h)
				# print(h,a,b)
			a = -1
			flag = False
print(maxArea)