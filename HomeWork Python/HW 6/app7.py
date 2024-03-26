numere = []

for i in range(4):
    numar = int(input("Introduceti un numar: "))
    numere.append(numar)

distincte = True

for i in range(len(numere)):
    for j in range(i+1, len(numere)):
        if numere[i] == numere[j]:
            distincte = False
            break

if distincte:
    print("Numerele sunt distincte.")
else:
    print("Numerele nu sunt distincte.")