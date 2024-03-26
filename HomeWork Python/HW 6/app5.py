num1 = int(input("Introduceti primul numar: "))
num2 = int(input("Introduceti al doilea numar: "))
num3 = int(input("Introduceti al treilea numar: "))

afirmatii_adevarate = 0

if num1 % 3 == 0 and num2 % 3 == 0 and num3 % 3 == 0:
    afirmatii_adevarate += 1

if (num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 != 0) or (num1 % 2 == 0 and num2 % 2 != 0 and num3 % 2 == 0) or (num1 % 2 != 0 and num2 % 2 == 0 and num3 % 2 == 0):
    afirmatii_adevarate += 1

if num1 > 10 and num2 > 10 and num3 > 10:
    afirmatii_adevarate += 1

print("Numarul de afirmatii adevarate este:", afirmatii_adevarate)