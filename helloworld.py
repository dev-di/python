#name = input("What is your name my friend? ") 
name = "Diana"
message = "Hello my friend, " + name + "!" 
print(message) #comment
print(message.upper())
print(message.capitalize())
print(message.count("i"))
print(f"message = '{message}', name = '{name}'")

print("Hello {}!!".format(name))
print("Hello {0}!".format(name))