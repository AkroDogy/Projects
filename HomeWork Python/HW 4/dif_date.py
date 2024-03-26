data1 = input("Introduceti prima data (yyyy,mm,dd): ")
data2 = input("Introduceti a doua data (yyyy,mm,dd): ")

data1 = list(data1.split(","))
data2 = list(data2.split(","))

diferenta  = int(data1[-1]) - int(data2[-1])
print(abs(diferenta))