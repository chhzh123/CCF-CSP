p = int(input())
app = {}
for i in range(p):
	lst = input().split(":")
	if len(lst) == 1:
		app[lst[0]] = None
	else:
		app[lst[0]] = int(lst[1])
r = int(input())
role = {}
for i in range(r):
	lst = input().split()
	dic = {}
	for a in lst[2:]:
		tmp = a.split(":")
		if len(tmp) == 1:
			dic[tmp[0]] = None
		else:
			dic[tmp[0]] = int(tmp[1])
	role[lst[0]] = dic
u = int(input())
user = {}
for i in range(u):
	lst = input().split()
	dic = {}
	for a in lst[2:]:
		for tmp in role[a]:
			if dic.get(tmp,-1) == -1 or dic.get(tmp) < role[a][tmp]:
				dic[tmp] = role[a][tmp]
	user[lst[0]] = dic
q = int(input())
for i in range(q):
	lst = input().split()
	user_q = lst[0]
	op = lst[1].split(":")
	if len(op) == 1:
		prio_q = None
	else:
		prio_q = int(op[1])
	op = op[0]
	if user.get(user_q,None) == None:
		print("false")
	else:
		dic = user[user_q]
		prio = dic.get(op,-1)
		if prio == -1: # wrong input
			print("false")
		elif prio == None: # app not priviledged
			print("true")
		else: # app priviledged
			if prio_q != None: # query priviledged
				if prio_q < prio:
					print("false")
				else:
					print("true")
			else: # query not priviledged
				print(prio)