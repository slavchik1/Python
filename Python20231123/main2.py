def Is_a_number_Prime(num):
    return_variable = True

    if num >= 2:
        for i in range(2, num):
            if num % i == 0:
                return_variable = False

    return return_variable


print(Is_a_number_Prime(int(input("Введіть число.\n"))))
