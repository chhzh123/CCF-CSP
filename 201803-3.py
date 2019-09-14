# NOT DONE YET! (70)

n, m = list(map(int,input().split()))
urlMapping = []
for i in range(n):
	s, name = input().split()
	urlMapping.append([name] + s.split("/")[1:])
for t in range(m):
	s = input()
	flag = True
	for i in range(len(s)):
		if not (s[i].isalnum() or s[i] == '/' or s[i] == '-' or s[i] == '_' or s[i] == '.'):
			flag = False
			break
	if not flag:
		break
	s = s.split("/")[1:]
	# print(s)
	for url in urlMapping:
		tmp = url[1:]
		flag = True
		res = []
		for (i,item) in enumerate(tmp):
			if i >= len(s):
				flag = False
				break
			# print("s[{}]={} item={}".format(i,s[i],item))
			if s[i] != item:
				if item == "<int>":
					if '-' in s[i]:
						flag = False
					else:
						try:
							res.append(int(s[i]))
						except:
							flag = False
				elif item == "<str>":
					if "/" in s[i] or s[i] == "":
						flag = False
					else:
						res.append(s[i])
				elif item == "<path>":
					path = ""
					for j in range(i,len(s)):
						path += s[j] + ("/" if j != len(s)-1 else "")
					res.append(path)
					break
				else:
					flag = False
			if not flag:
				break
		# print()
		if flag:
			break
	if flag:
		print(url[0],end=" " if len(res) != 0 else "\n")
		for i in range(len(res)):
			print(res[i],end=" " if i != len(res)-1 else "\n")
	else:
		print("404")