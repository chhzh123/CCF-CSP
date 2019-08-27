n = int(input())
segment = [0] * 1000005
for i in range(n):
	a, b = list(map(int,input().split()))
	for t in range(a,b):
		segment[t] = 1
res = 0
for i in range(n):
	a, b = list(map(int,input().split()))
	for t in range(a,b):
		if segment[t] == 1:
			res += 1
print(res)