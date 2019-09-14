import calendar
cal = calendar.Calendar()
a,b,c,y1,y2 = list(map(int,input().split()))
for year in range(y1,y2+1):
	try:
		day = list(cal.itermonthdays(year,a))[(b-1)*7+c-1]
		if day != 0:
			print("{:0>4d}/{:0>2d}/{:0>2d}".format(year,a,day))
		else:
			print("none")
	except:
		print("none")