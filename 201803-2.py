n, L, t = list(map(int,input().split()))
ball = list(map(int,input().split()))
ball = [[b,1] for b in ball]
for time in range(t):
	pos = []
	for j in range(L+1):
		pos.append([])
	for i in range(len(ball)):
		ball[i][0] += ball[i][1]
		if ball[i][0] >= L:
			ball[i][0] = L
			ball[i][1] = -1
		elif ball[i][0] <= 0:
			ball[i][0] = 0
			ball[i][0] = 1
		pos[ball[i][0]].append(i)
	# collision
	for i in range(len(ball)):
		if len(pos[ball[i][0]]) > 1:
			ball[i][1] *= -1
for i in range(len(ball)):
	print(ball[i][0],end=(" " if i != len(ball)-1 else "\n"))

# Notice Example 2 is wrong!