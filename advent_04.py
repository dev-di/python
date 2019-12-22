
import math

def check_non_decrease(password):
    if password < 10:
        return True
    else:
        last_digit = password%10
        rest_parts = password//10
        second_last_digit = rest_parts%10
        return last_digit >=  second_last_digit and check_non_decrease(rest_parts)

def check_adjacency(password):
    if password < 10:
        return False
    else:
        last_digit = password%10
        rest_parts = password//10
        second_last_digit = rest_parts%10
        return last_digit == second_last_digit or check_adjacency(rest_parts)

def check_criterium(password):
    return check_non_decrease(password) and check_adjacency(password)

moduleInput = [372304,847060]
#print(moduleInput)
password_range = range(moduleInput[0], moduleInput[1])

print(len(password_range))

filtered_range = filter(check_criterium, password_range)



#for password in filtered_range:
#   print(password)


print(len(tuple(filtered_range)))