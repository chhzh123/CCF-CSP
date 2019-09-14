# NOT DONE YET! (90)

n, m = list(map(int,input().split()))
d = {}
s = ""
for i in range(n):
	s += input()
d = eval(s)
for i in range(m):
	query = input().split('.')
	p = d
	flag = True
	for q in query:
		p = p.get(q,None)
		if p == None:
			print("NOTEXIST")
			flag = False
			break
		elif type(p) == type("str"):
			print("STRING",str(p))
			flag = False
			break
	if flag:
		print("OBJECT")