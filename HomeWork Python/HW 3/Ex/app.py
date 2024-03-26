def app_1():
    n = input(" >> Introdu sirul de caractere: ")
    print(f"Sirul il contine pe (a) de {n.count('a')}")
    print(f"Textul introdus este: {n}\n-------\nVocale:")
    print(f"a -  {n.count('a')}")
    print(f"e -  {n.count('e')}")
    print(f"i -  {n.count('i')}")
    print(f"o -  {n.count('o')}")
    print(f"u -  {n.count('u')}")
    print("-------")
    print("Total vocale:")
    print(f"{n.count('a')+n.count('e')+n.count('i')+n.count('o')+n.count('u')}")

if __name__ == "__main__":
    app_1()