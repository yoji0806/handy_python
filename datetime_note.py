from datetime import date, timedelta

'''
print all day-date between two dates
'''
sdate = date(2018, 12, 7)   # start date
edate = date(2018, 12, 18)   # end date

delta = edate - sdate       # as timedelta

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    print(day)