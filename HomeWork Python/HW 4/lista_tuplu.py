#Scrieți un program Python care acceptă de la utilizator o secvență de
#numere separate prin virgulă și generează o listă și un tuplu din acele numere.
#Date eșantion: 3, 5, 7, 23


n = input("Introduceti numerele separate prin virgula: ")
lista = n.split(",")
tuplu = tuple(lista)

print("Lista: ", lista)
print("Tuplu: ", tuplu)
