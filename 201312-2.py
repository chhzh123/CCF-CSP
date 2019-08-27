isbn = input()
l = isbn.split('-')
s = ""
for i in range(len(l)):
	s += l[i]
res = 0
for i in range(len(s)-1):
	res += (i+1) * int(s[i])
mod = res % 11
if s[-1] == "X":
	if mod == 10:
		print("Right")
	else:
		print(isbn[:-1] + str(mod))
elif mod == int(s[-1]): # s[-1] != "X"
	print("Right")
else:
	if mod == 10:
		print(isbn[:-1] + "X")
	else:
		print(isbn[:-1] + str(mod))