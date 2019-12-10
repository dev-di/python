
price = 0
if price > 1.0:
    tax = 0.7
else: 
    tax = 0

print("Tax: " + str(tax))

name = "Diana"
if name.upper() == "DIANA":
    print("Hello queen!")
elif name.upper().endswith("BANAN") or name.upper().endswith("BANANA"):
    print("Hello banan!")
else: 
    print("Hello.")


if name in ('Diana','Juliana'):
    print("Queen name!")
else: 
    print("Good day!")