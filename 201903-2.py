def sign(sig):
	if sig == '+':
		return '+'
	elif sig == '-':
		return '-'
	elif sig == 'x':
		return '*'
	else:
		return "//"

n = int(input())
for i in range(n):
	s = input()
	res = 0
	# a, b, c, d = int(s[0]), int(s[2]), int(s[4]), int(s[6])
	a, b, c, d = s[0], s[2], s[4], s[6]
	s = a + sign(s[1]) + b + sign(s[3]) + c + sign(s[5]) + d
	res = eval(s)
	if res == 24:
		print("Yes")
	else:
		print("No")

# 10
# 9+3+4x3
# 5+4x5x5
# 7-9-9+8
# 5x6/5x4
# 3+5+7+9
# 1x1+9-9
# 1x9-5/9
# 8/5+6x9
# 6x7-3x6
# 6x4+4/5