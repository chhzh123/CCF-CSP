a = []
for i in range(15):
	a.append(list(map(int,input().split())))
s = []
for i in range(4):
	lst = list(map(int,input().split()))
	if 1 in lst:
		s.append(lst)
p = []
for i in range(len(s)):
	for j in range(4):
		if s[i][j] == 1:
			p.append((len(s)-i-1,j))
n = int(input()) - 1
for i in range(14,-1,-1):
	flag = True
	for ele in p:
		if a[i-ele[0]][n+ele[1]] == 1:
			flag = False
			break
	if flag: # need to be very careful!
		for ele in p:
			for j in range(i-ele[0]-1,-1,-1):
				if a[j][n+ele[1]] == 1:
					flag = False
					break
		if flag == False:
			continue
		for ele in p:
			a[i-ele[0]][n+ele[1]] = 1
		break
for i in range(15):
	for j in range(10):
		print(a[i][j],end=(" " if j != 9 else "\n"))