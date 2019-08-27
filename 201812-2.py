# NOT DONE YET! (20)

r, y, g = list(map(int,input().split()))

def changeLED(led,t):
	while led[1] < t:
		if led[0] == 1:
			led[0] = 3
		elif led[0] == 2:
			led[0] = 1
		else:
			led[0] = 2
		if led[0] == 1:
			led[1] += r
		elif led[0] == 2:
			led[1] += y
		else:
			led[1] += g
	led[1] -= t

n = int(input())
lightIndex = []
roads = []
for i in range(n):
	k, t = list(map(int,input().split()))
	roads.append([k,t])
	if k != 0:
		lightIndex.append(i)
res = 0
for i in range(n):
	# print(roads)
	k, t = roads[i]
	if k == 0:
		res += t
		for l in lightIndex:
			changeLED(roads[l],t)
	elif k == 1:
		res += t
		for l in lightIndex:
			changeLED(roads[l],t)
	elif k == 2:
		res += t
		for l in lightIndex:
			changeLED(roads[l],t)
	else: # green
		pass
print(res)