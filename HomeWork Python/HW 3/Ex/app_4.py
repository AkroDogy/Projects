def app_1():
    n_1 = input("Numar 1:")
    n_2 = input("Numar 2:")
    if n_1 == 0 or n_2 == 0 or n_1 == n_2:
        print("Nu se pot afisa cu aceste numere.")
    else:
        print(f"{n_1}{n_2} {n_2}{n_1}")


if __name__ == "__main__":
    app_1()