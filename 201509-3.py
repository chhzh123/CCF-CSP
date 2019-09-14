m, n = list(map(int,input().split()))
pos = []
template = []
for i in range(m):
	tmp = input().split("{{ ")
	pos.append([])
	for (j,t) in enumerate(tmp):
		if j == 0:
			continue
		t = t.split(" }}")
		pos[-1].append(t[0]) # var
		tmp[j] = t[-1] # rest of the string
	template.append(tmp)
# print(pos)
varlist = {}
for i in range(n):
	var, target = input().split(" \"")
	varlist[var] = target[:-1]
# print(varlist)
for i in range(m):
	res = ""
	for (j,s) in enumerate(template[i]):
		if j >= len(pos[i]):
			res += s
		else:
			res += s + varlist.get(pos[i][j],"")
	print(res)