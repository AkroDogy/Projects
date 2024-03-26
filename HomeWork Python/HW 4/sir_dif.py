#Scrieți un program Python pentru a obține un șir format din primele 2 și
#ultimele 2 caractere ale unui șir dat. Dacă lungimea șirului este mai mică de 2,
#returnați în schimb șirul gol.

n = input("Introdu sirul: ")
if len(n) < 2:
    print(" ")
else:
    print(n[:2] + n[-2:])

