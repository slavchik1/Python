list = []

number_of_e_adresses = int(input("Введіть кількість електроних адрес. \n"))

for i in range(number_of_e_adresses):
    list.append(input("Введіть електрону адресу. \n"))

for i in range(number_of_e_adresses):
    e_adress = list[i]
    e_adress_in_list_fourm = [char for char in e_adress]
    len_of_e_adress = len(e_adress_in_list_fourm)

    if e_adress_in_list_fourm[len_of_e_adress - 12] == "@" and e_adress_in_list_fourm[len_of_e_adress - 11] == "e" and e_adress_in_list_fourm[len_of_e_adress - 10] == "x" and e_adress_in_list_fourm[len_of_e_adress - 9] == "a" and e_adress_in_list_fourm[len_of_e_adress - 8] == "m" and e_adress_in_list_fourm[len_of_e_adress - 7] == "p" and e_adress_in_list_fourm[len_of_e_adress - 6] == "l" and e_adress_in_list_fourm[len_of_e_adress - 5] == "e" and e_adress_in_list_fourm[len_of_e_adress - 4] == "." and e_adress_in_list_fourm[len_of_e_adress - 3] == "c" and e_adress_in_list_fourm[len_of_e_adress - 2] == "o" and e_adress_in_list_fourm[len_of_e_adress - 1] == "m":
        print(e_adress)

