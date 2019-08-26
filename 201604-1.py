n = int(input())
a = list(map(int,input().split()))
if n <= 2:
	print("0")
else:
	res = 0
	for i in range(1, len(a) - 1):
		if (a[i-1] > a[i] and a[i] < a[i+1]) or (a[i-1] < a[i] and a[i] > a[i+1]):
			res += 1
	print(res)