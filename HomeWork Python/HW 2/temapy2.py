def app_1():
    n = int(input("Alege cat de mare vrei sa fie functia: "))
    print("a) E=", end="")
    for x in range(2, n+2):
        print(f"1/{x} + ", end="")
    print("\b\b ")
    print("\nb) E=", end="")
    for y in range(2, n+2):
        print(f"1/{y}x{y+1} + ", end="")
    print("\b\b ")
    print("\nc) E=", end="")
    for z in range(1, n**2+1, 4):
        print(f"{z}+{z+1}/{z+2}+{z+3} + ", end="")
    print("\b\b ")
    return " "

def app_2():
    x = int(input(" Numar: "))
    print(bool(x+7==x*8))
    return not bool(2*x+3==6)

def app_3():
    return " La subpunctul a nu este inchisa paranteza rotunda <Corect: (x+3)>\n La subunctul b nu se poate face calcul un numar cu un string <Corect: transformam stringul intr-un numar de tip int sau float> \n La subpunctul c aceeasi problema ca la subpunctul a <Corect: (x+1)/((x+2)-1)\n"

def app_4():
    a = 2
    b = 5
    print(eval('True == a<b'))
    print(eval('True == (a<b)'))
    print(eval('not a+b'))
    print(eval('a == a+b+1'))
    return ""

def app_5():
    x = int(input(" Volum: "))
    return f"Decilitrii: {x*10}, Centilitrii: {x*100}, Mililitrii: {x*1000}"

def app_6():
    n = str(input(" Ce cifre vrei sa scrii de la dreapta la stanga: "))
    return n[::-1]

def app_7():
    x = str(input(" Valori interschimbate: "))
    return f"{x[1]}{x[0]}{x[2]}"

def app_8():
    x = str(input(" Numar de 2 cifre: "))
    return ((int(x[0])*int(x[0]))+(int(x[1])*int(x[1])))

def app_9():
    x = str(input(" Numar de 5 cifre se afiseaza suma lor: "))
    return int(x[0])+int(x[1])+int(x[2])+int(x[3])+int(x[4])

def app_10():
    x = str(input(" Numar de 5 cifre se afiseaza produsul lor: "))
    return int(x[0])*int(x[1])*int(x[2])*int(x[3])*int(x[4])

def app_11():
    medie = 0
    j_ = []
    x = int(input("Cati elevi doresti sa adaugi?: "))
    for i in range(0, x):
        print("Medie elev", i+1)
        medie_elev = float(input())
        j_.append(medie_elev)
        medie += medie_elev
    return medie/x

def app_12():
    n = int(input("N = "))
    m = int(input("M = "))
    if n < 0 or m < 0:
        return "Numerele trebuiesc sa fie pozitive"
    else:
        return 2**n+m


def menu(m_number):
    if m_number == 0:
        return app_1()
    elif m_number == 1:
        return app_2()
    elif m_number == 2:
        return app_3()
    elif m_number == 3:
        return app_4()
    elif m_number == 4:
        return app_5()
    elif m_number == 5:
        return app_6()
    elif m_number == 6:
        return app_7()
    elif m_number == 7:
        return app_8()
    elif m_number == 8:
        return app_9()
    elif m_number == 9:
        return app_10()
    elif m_number == 10:
        return app_11()
    elif m_number == 11:
        return app_12()

if __name__ == "__main__":
    print(">> TEME <<")
    print("")
    for i in range(0,12):
        print(f"{i} - EX.{i+1}")
    print("")
    print("--------------------------------")
    m_number = int(input(" >> Alege un Numar de la 0 la 11 pentru a accesa un excertitiu: "))
    print(menu(m_number))