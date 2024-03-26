#Scrieți un program Python pentru a număra numărul de caractere
#(frecvența caracterelor) dintr-un șir. (dict)

n = input("Introdu sirul")
dict = {}
for i in n:
    keys = dict.keys()
    if i in keys:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

