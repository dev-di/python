# This is how to import in Python
from datetime import datetime, timedelta

# birth = input("What is your birth date? (yyyy-mm-dd): ")
birth = "2019-11-13"
birthday_date = datetime.strptime(birth, "%Y-%m-%d")
print("Your birthdate is: " + str(birthday_date))
print("Your day of birth was a: " + str(birthday_date.weekday()))
print(birthday_date.weekday)
print(birthday_date)


