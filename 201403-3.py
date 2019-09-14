s = input()
n = int(input())
dic = {}
for i in range(len(s)):
	if s[i] == ':':
		continue
	elif i+1 == len(s) or s[i+1] != ':':
		dic[s[i]] = False
	else:
		dic[s[i]] = True # with arguments
for i in range(n):
	res = {}
	args = input().split()[1:]
	j = 0
	while j < len(args):
		if args[j][0] == '-':
			if dic.get(args[j][-1],'E') != 'E':
				if not dic[args[j][-1]]:
					res[args[j]] = ""
				else: # with arguments
					if j + 1 < len(args) and args[j+1][0] != '-':
						res[args[j]] = args[j+1]
						j += 1
					else:
						break
			else:
				break
		else:
			break
		j += 1
	res = sorted(res.items())
	print("Case {}:".format(i+1),end="")
	for j in range(len(res)):
		if res[j][1] == "":
			print(" {}".format(res[j][0]),end="")
		else:
			print(" {} {}".format(res[j][0],res[j][1]),end="")
	print()