p = 0

num1 = int(input("Introduceti primul numar: "))
num2 = int(input("Introduceti al doilea numar: "))
num3 = int(input("Introduceti al treilea numar: "))

if num1 % 2 == 0:
    p += 1
if num2 % 2 == 0:
    p += 1
if num3 % 2 == 0:
    p += 1

print("Numarul de valori pare este:", p)