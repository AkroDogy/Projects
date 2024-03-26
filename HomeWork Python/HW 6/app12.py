litera = input("Introduceți o literă: ")

if litera.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Litera introdusă este o vocală.")
else:
    print("Litera introdusă este o consoană.")

sir = input("Introduceți un șir de caractere: ")
primul_caracter = sir[0].lower()
ultimul_caracter = sir[-1].lower()

if primul_caracter in ['a', 'e', 'i', 'o', 'u'] and ultimul_caracter in ['a', 'e', 'i', 'o', 'u']:
    print("Primul și ultimul caracter sunt vocale.")
else:
    print("Primul și ultimul caracter nu sunt vocale.")