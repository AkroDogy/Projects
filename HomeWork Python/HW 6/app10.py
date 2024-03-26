def numar(numar1, numar2):
    penultima_cifra1 = (numar1 // 10) % 10
    penultima_cifra2 = (numar2 // 10) % 10

    if penultima_cifra1 > penultima_cifra2:
        return numar1
    elif penultima_cifra2 > penultima_cifra1:
        return numar2
    else:
        return "Ambele numere au aceeasi penultima cifra"

# Exemplu de utilizare
numar1 = int(input("Introduceti primul numar: "))
numar2 = int(input("Introduceti al doilea numar: "))
numar_mai_mare = numar(numar1, numar2)
print(f"Numarul cu penultima cifra mai mare este: {numar_mai_mare}")