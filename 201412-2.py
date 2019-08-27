n = int(input())
a = []
for i in range(n):
	a.append(list(map(int,input().split())))
for i in range(n):
	if i % 2 == 0:
		for k in range(i,-1,-1):
			print(a[k][i-k],end=" ")
	else:
		for k in range(i+1):
			print(a[k][i-k],end=" ")
for i in range(n):
	if (n % 2 == 0 and i % 2 == 1) or (n % 2 == 1 and i % 2 == 0):
		for k in range(i+1,n):
			# print(k,i-k)
			print(a[k][i-k],end=("\n" if (k == n-1 and i-k == -1) else " "))
	else:
		for k in range(n-1,i,-1):
			# print(k,i-k)
			print(a[k][i-k],end=("\n" if (k == n-1 and i-k == -1) else " "))

# 3
# 1 5 3
# 3 7 5
# 9 4 6