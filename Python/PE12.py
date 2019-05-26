from datetime import *

year,month,day=1901,1,1
count_=0
cur_day=date(year,month,day)

while (cur_day.year<2001):
	if (cur_day.weekday()==6):
		count_+=1
	if (cur_day.month + 1) == 13:
		month=1
		year+=1
	else:
		month+=1
	cur_day=date(year,month,1)

print(count_)