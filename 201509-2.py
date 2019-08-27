y = int(input())
d = int(input())
month = [31,28,31,30,31,30,31,31,30,31,30,31]
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
	month[1] += 1
res = 0
for i in range(len(month)):
	if res + month[i] < d:
		res += month[i]
	else:
		print(i+1)
		print(d-res)
		break