import time
import calendar

MONTH = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
WEEK = {"Sun":0,"Mon":1,"Tue":2,"Wed":3,"Thu":4,"Fri":5,"Sat":6}

def parse(s,range_lst,name_dict=None):
	lst = []
	if s == "*":
		lst = range_lst
	else:
		s_str = s.split(",")
		for m in s_str:
			if '-' not in m:
				lst.append(int(m) if m.isdigit() else name_dict[m])
			else:
				a,b = m.split("-")
				a = int(a) if a.isdigit() else name_dict[a]
				b = int(b) if b.isdigit() else name_dict[b]
				for j in range(a,b+1):
					lst.append(j)
	return lst

n, s, e = input().split()
start = time.strptime(s,"%Y%m%d%H%M")
end = time.strptime(e,"%Y%m%d%H%M")
res = []
for i in range(int(n)):
	minutes, hours, day_of_month, month, day_of_week, command = input().split()
	month_list = parse(month,range(1,13),MONTH)
	day_list = parse(day_of_month,range(1,32))
	week_list = parse(day_of_week,range(1,8),WEEK)
	week_list = [week-1 if week-1 >= 0 else 6 for week in week_list]
	hour_list = parse(hours,range(0,24))
	minute_list = parse(minutes,range(0,60))
	Cal = calendar.Calendar()
	# print(month_list)
	# print(day_list)
	# print(week_list)
	# print(hour_list)
	# print(minute_list)
	for year in range(start.tm_year,end.tm_year+1):
		for month in month_list:
			for date in Cal.itermonthdates(year,month):
				if date.day in day_list and date.weekday() in week_list:
					for hour in hour_list:
						for minute in minute_list:
							string = "{:0>4d}{:0>2d}{:0>2d}{:0>2d}{:0>2d}".format(year,month,date.day,hour,minute)
							if s <= string < e:
								res.append((string,command))
res.sort()
for q in res:
	print(q[0],q[1])