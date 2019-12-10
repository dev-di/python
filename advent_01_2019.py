import input_module

moduleInput = input_module.get_integer_lines_as_list('input/advent_input_01.txt')
#moduleInput = [14,1969]
print(moduleInput)

def calculate_fuel_requirement(mass):
    return max(int(mass/3)-2,0)

def extended_fuel_requirement(mass):
    f=calculate_fuel_requirement(mass)
    sum=0
    while f>0:
        sum+=f
        f = calculate_fuel_requirement(f)
    return sum

fuelSum = 0
for i in moduleInput:
    f = extended_fuel_requirement(i)
    print("Total for module with mass {0}: {1}".format(i, f))
    fuelSum += f

print("\nsum: ")
print(fuelSum)