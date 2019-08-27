a = []
for i in range(20):
	a.append([0]*5)

def getTickets(nTickets):
	res = []
	for i in range(20):
		for j in range(5):
			if nTickets > 5 - j:
				break
			flag = True
			for k in range(nTickets):
				if a[i][j+k] != 0:
					flag = False
					break
			if flag:
				for k in range(nTickets):
					a[i][j+k] = 1
				res = [i*5+j+1+k for k in range(nTickets)]
				return res
	res = []
	cnt = 0
	for i in range(20):
		flag = False
		for j in range(5):
			if a[i][j] == 0:
				cnt += 1
				a[i][j] = 1
				res.append(i*5+j+1)
				if cnt == nTickets:
					flag = True
					break
		if flag:
			break
	return res

n = int(input())
p = list(map(int,input().split()))
for pi in p:
	res = getTickets(pi)
	for t in range(len(res)):
		print(res[t],end=(" " if t != len(res) - 1 else "\n"))