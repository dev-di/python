from datetime import datetime

#This is a function, it has to be defined before we can use it
#The message parameter has a default value
def printtime(message="Hejsan"):
    print(message)
    print(datetime.now())

printtime
printtime()
printtime("Good day")
printtime(message="halloj!") #using of named notation