n = int(input("Cate dictionare vrei? "))
dict_list = {}
for i in range(n):
    m = int(input(f"Cate elemente vrei sa fie in dictionarul {i+1}? "))
    temp_dict = {}
    for j in range(m):
        key = input("Introdu cheia: ")
        value = input("Introdu valoarea: ")
        temp_dict[key] = value
    dict_list.update(temp_dict)

print(dict_list)