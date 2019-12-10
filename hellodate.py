# This is how to import in Python
from datetime import datetime, timedelta

current_date = datetime.now()
one_day_time_interval = timedelta(days=1)

print(current_date)
print(str(current_date))
print("Day today: " +str(current_date.day))

yesterday = current_date - one_day_time_interval

print("Yesterday = {}".format(yesterday))