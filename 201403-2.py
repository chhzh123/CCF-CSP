# DO NOT USE ARRAY TRAVERSAL!!! WILL RUN OUT OF TIME!

n, m = map(int,input().split())
a = []
for x in range(2600):
	a.append([0]*1500)
win = []
for i in range(1,n+1):
	x1, y1, x2, y2 = map(int, input().split())
	win.append((x1,y1,x2,y2))
	for x in range(x1,x2+1):
		a[x][y1:y2+1] = [i] * (y2-y1+1) # important!
for i in range(m):
	x, y = map(int,input().split())
	if a[x][y] == 0:
		print("IGNORED")
	else:
		winIndex = a[x][y]
		print(winIndex)
		x1, y1, x2, y2 = win[winIndex-1]
		for x in range(x1,x2+1):
			a[x][y1:y2+1] = [winIndex] * (y2-y1+1)