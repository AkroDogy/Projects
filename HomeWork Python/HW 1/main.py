from colorama import init, Fore, Style

def app_1():
    num_1 = int(input())
    if num_1 < 0:
        return " >> Poti alege doar un numar natural"
    else:
        sum_1 = num_1 * 5
        return f"Produsul dintre {num_1} si 5 este: {sum_1}"

def app_2():
    num_a_2 = int(input())
    num_b_2 = int(input())
    sum_2 = num_a_2 * num_b_2
    return f"Produsul dintre {num_a_2} si {num_b_2} este: {sum_2}"

def app_3():
    num_a_3 = int(input())
    num_b_3 = int(input())
    sum_a_3 = num_a_3//num_b_3
    sum_b_3 = num_a_3%num_b_3
    return f"Catul intreg a celor doua numere este: {sum_a_3}, iar restul este: {sum_b_3}"

def app_4():
    num_a_4 = int(input())
    num_b_4 = int(input())
    if num_a_4 or num_b_4 < 0:
        return " >> Poti alege doar un numar natural"
    else:
        sum_a_4 = num_a_4+num_b_4
        dif_4 = num_a_4-num_b_4
        prod_4 = num_a_4*num_b_4
        cat_4 = num_a_4//num_b_4
        return f" Suma = {sum_a_4}, Diferenta = {dif_4}, Produs = {prod_4}, Catul Intreg: {cat_4}"

def app_5():
    num_5 = int(input())
    if num_5 < 2 or num_5 > 9:
        return " >> Numarul trebuie sa fie intre 2 si 9."
    else:
        for i in range(1, 10):
            print (f"{num_5} x {i} = {num_5 * i}")
        return f" >> Tabla inmultiri pentru numarul {num_5}"

def app_6():
    num_6 = input()
    num_b_6 = input()
    if num_6 == 0 or num_b_6 == 0:
        return " Numarul trebuie sa fie nenul"
    if num_6 == num_b_6:
        return "Numerele trebuie sa fie distincte"
    else:
        print(num_6 + num_b_6)
        print(num_b_6 + num_6)
        return " >> Done"

def app_7():
    fa ="*********\n"
    fa +="* @   @ *\n"
    fa +="*   *   *\n"
    fa +="*  \_/  *\n"
    fa +="*********"
    return fa

def app_8():
    num_8 = int(input())
    if num_8 < 0:
        return " >> Poti alege doar un numar natural"
    else:
        print(f"N la puterea a doua este {num_8**2}\n")
        print(f"N la puterea a treia este {num_8**3}")
        return ""

def app_9():
    init()
    nume = str(input(">> Introduceti numele: "))
    corporatie = str(input(">> Introduceti corporatia: "))
    descriere = str(input(">> Introduceti descrierea: "))
    post = str(input(">> Introduceti postul: "))
    le_va= len(nume)+len(corporatie)+3
    le_vb= len(descriere)+2
    if le_va < le_vb:
        ran = le_vb
    else:
        ran = le_va
    for i in range(1, ran+10):
        print("*", end="")
    print("\n")
    print(f">> {Style.BRIGHT}{corporatie}{Style.RESET_ALL}   {nume} ")
    print(f">>          {Style.BRIGHT}{post}{Style.RESET_ALL}")
    print(f"")
    print(f">>  {descriere} ")
    print(f"")
    for i in range(1, ran+10):
        print("*", end="")
    return ""
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

if __name__ == "__main__":
    print(">> TEME <<")
    print("")
    for i in range(0,9):
        print(f"{i} - EX.{i+1}")
    print("")
    print("--------------------------------")
    m_number = int(input(" >> Alege un Numar de la 0 la 8 pentru a accesa un excertitiu: "))
    print(menu(m_number))

