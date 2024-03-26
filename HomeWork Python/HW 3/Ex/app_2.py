def app_1():
    n = input(" >> Introdu sirul de caractere: ")
    print(f"a) Lungimea sirului: {len(n)}")
    if n.count('x') >= 1:
        print(f"b) Il contine pe x?: DA")
    else:
        print(f"b) Il contine pe x?: NU")
    if n.startswith('a') or n.startswith('A'):
        print(f"c) Incepe cu a sau A?: DA")
    else:
        print(f"c) Incepe cu a sau A?: NU")
    if n.endswith('.'):
        print(f"d) Se termina cu .?: DA")
    else:
        print(f"d) Se termina cu .?: NU")

if __name__ == "__main__":
    app_1()