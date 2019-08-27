n = int(input())
cases = int(input())
a = [i for i in range(n)]
for t in range(cases):
	p, q = list(map(int,input().split()))
	p = a.index(p-1)
	if q > 0:
		a[p:p+q+1] = a[p:p+q+1][1:] + [a[p:p+q+1][0]]
	else:
		a[p+q:p+1] = [a[p+q:p+1][-1]] + a[p+q:p+1][:-1]
for i in range(len(a)):
	print(a[i]+1,end=" " if i != len(a)-1 else "\n")