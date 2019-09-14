# NOT DONE YET! RUNTIME ERROR(90)

m, n, q = list(map(int,input().split()))
a = []

def fill(x,y,c):
	if x < 0 or x >= m or y < 0 or y >= n:
		return
	if a[x][y] in ['-','|','+',c]:
		return
	else:
		a[x][y] = c
		fill(x-1,y,c)
		fill(x+1,y,c)
		fill(x,y-1,c)
		fill(x,y+1,c)

# m(x) * n(y)
for i in range(m):
	a.append(['.'] * n)
for t in range(q):
	op = input().split()
	if int(op[0]) == 0: # draw line (x1,y1,x2,y2)
		op = list(map(int,op))
		if op[1] == op[3]: # the same x
			d = min(op[2],op[4])
			u = max(op[2],op[4])
			for j in range(d,u+1):
				if a[op[1]][j] in ['-','+']: # be careful!
					a[op[1]][j] = '+'
				else:
					a[op[1]][j] = '|'
		else: # the same y
			l = min(op[1],op[3])
			r = max(op[1],op[3])
			for i in range(l,r+1):
				if a[i][op[2]] in ['|','+']:
					a[i][op[2]] = '+'
				else:
					a[i][op[2]] = '-'
	else:
		fill(int(op[1]),int(op[2]),op[3])
for j in range(n-1,-1,-1):
	for i in range(m):
		print(a[i][j],end="" if i != m-1 else "\n")