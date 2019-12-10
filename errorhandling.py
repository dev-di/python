from datetime import datetime

birth = input("What is your birth date? (yyyy-mm-dd): ")

try:
    birthday_date = datetime.strptime(birth, "%Y-%m-%d")
    print("Thank you!")
except ValueError as e:
    print("error: " +str(e))
    print("Format not acceped!")
    
print("Goodbye")
