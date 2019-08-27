n, k = list(map(int,input().split()))
maxT = 0
keys = [i for i in range(n)]
timepoint = []
for i in range(k):
	w, s, c = list(map(int,input().split()))
	timepoint.append((w-1,s,0))
	timepoint.append((w-1,s+c,1))
	maxT = max(maxT,s+c)
# first return keys (x[2]) in ascending order (x[0])
timepoint.sort(key=lambda x: (x[1],-x[2],x[0]))
for t in timepoint:
	if t[2] == 0:
		for i in range(n):
			if keys[i] == t[0]:
				keys[i] = "X"
				break
	else:
		for i in range(n):
			if keys[i] == "X":
				keys[i] = t[0]
				break
for i in range(n):
	print(keys[i]+1,end=" " if i != n-1 else "\n")