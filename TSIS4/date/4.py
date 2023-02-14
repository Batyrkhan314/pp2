'''Write a Python program to calculate two date difference in seconds.'''

from datetime import datetime

def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2022-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')


date2 = datetime.now()
print(str(date_diff_in_Seconds(date2,date1)) + " seconds")
print()