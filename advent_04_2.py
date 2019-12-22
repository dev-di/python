
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
    password_str = str(password)
    digit_array = [ch for ch in password_str]
    for index in range(1, len(digit_array)-2):
        if digit_array[index] == digit_array[index+1] and digit_array[index+1] != digit_array[index+2] and digit_array[index+1] != digit_array[index-1]:
            return True
    if digit_array[0] == digit_array[1] and digit_array[1] != digit_array[2]:
        return True
    N = len(digit_array)
    if digit_array[N-1] == digit_array[N-2] and digit_array[N-2] != digit_array[N-3]:
        return True
    return False

def check_criterium(password):
    return check_non_decrease(password) and check_adjacency(password)

moduleInput = [372304,847060]
password_range = range(moduleInput[0], moduleInput[1])

print(check_adjacency(11234111111))

filtered_range = filter(check_criterium, password_range)

#for password in filtered_range:
#    print(password)


print(len(tuple(filtered_range)))