t = int(input())
for s in range(t // 100, 1005):
	a = s * 100 - 3500
	res = s * 100
	tax = int(max(0,min(a,1500)) * 0.03 + max(0,min(a-1500,4500-1500)) * 0.1 + max(0,min(a-4500,9000-4500)) * 0.2 + max(0,min(a-9000,35000-9000)) * 0.25 + max(0,min(a-35000,55000-35000)) * 0.3 + max(0,min(a-55000,80000-55000)) * 0.35 + max(0,a-80000) * 0.45)
	if res - tax == t:
		print(res)
		break