
numar1 = int(input("Introdu primul număr: "))
numar2 = int(input("Introdu al doilea număr: "))

if numar1 % numar2 == 0:
    print(f"{numar1} se împarte perfect cu {numar2}")
else:
    print(f"{numar1} nu se împarte perfect cu {numar2}")