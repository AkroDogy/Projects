
numar = int(input("Introdu un număr format din două cifre: "))

cifra_zeci = numar // 10
cifra_unitati = numar % 10

suma = cifra_zeci + cifra_unitati

if suma % 2 == 0:
    print("Suma cifrelor este pară.")
else:
    print("Suma cifrelor este impară.")