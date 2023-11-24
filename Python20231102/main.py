list = []

number_of_poducts = int(input("Введіть кількість товарів. \n"))

for i in range(number_of_poducts):
    name_op_product = input("Введіть назву товару. \n")
    price_of_product = float(input("Введіть ціну товару (₴). \n"))
    amout_of_product = int(input("Введіть кількість товару \n"))

    list.append([name_op_product, price_of_product, amout_of_product])

sum_of_prices_of_products = 0

for i in range(number_of_poducts):
    sum_of_prices_of_products += list[i][1] * list[i][2]

tax_of_prices_of_products = sum_of_prices_of_products * 0.18

print("Загальна сума покупки: " + str(sum_of_prices_of_products) + "\nСума податків: " + str(tax_of_prices_of_products))

for i in range(number_of_poducts):
    print(list[i][0] + " - " + str(list[i][1]) + " - " + str(list[i][2]) + " - " + str(list[i][1] * list[i][2]))
