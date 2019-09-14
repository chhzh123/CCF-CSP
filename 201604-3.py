# catalog = {"/":["/","d1","d2"],
# 	"d1":["/","f1","f2"],
# 	"d2":["/","d3","d4","f4"],
# 	"d3":["d2","f3"],
# 	"d4":["d2","f1"]}
# n = int(input())
# curr = input().split('/')
# p = catalog[curr[-1]]
# for i in range(n):
# 	path = input().split('/')
# 	abspath = []
# 	if path[0] == "":
# 		p = catalog["/"]
# 	else:
# 		abspath = curr.copy()[1:]
# 	for folder in path:
# 		if folder == "." or folder == "":
# 			continue
# 		elif folder == "..":
# 			p = catalog[p[0]]
# 			abspath = abspath[:-1]
# 		else:
# 			if folder in catalog.keys():
# 				p = catalog[folder]
# 			abspath.append(folder)
# 	res = ""
# 	if len(abspath) == 0:
# 		res = "/"
# 	else:
# 		for folder in abspath:
# 			res += "/" + folder
# 	print(res)

# NOT DONE YET! (90)

n = int(input())
curr = input().split('/')
for i in range(n):
	path = input().split('/')
	if not path[0] == "":
		abspath = curr.copy()[1:]
	else:
		abspath = []
	for folder in path:
		if folder == "." or folder == "":
			continue
		elif folder == "..":
			abspath = abspath[:-1]
		else:
			abspath.append(folder)
	res = ""
	if len(abspath) == 0:
		res = "/"
	else:
		for folder in abspath:
			res += "/" + folder
	print(res)