import sys


products = {}


def help():
    print("""Список команд:

help - список команд.
add_product - додати продукт.
delete_product - удалити продукт.
show_product - показати продукти.
exit - вийти з програми.
""")


def add_product():
    name = input("Введіть назву продукта.\n")
    count = int(input("Введіть кількість товару.\n"))
    price = float(input("Введіть ціну товару.\n"))

    products[name] = {
        "count": count,
        "price": price
    }

    print("\nПродукт додано.\n")


def delete_product():
    name = input("Введіть назву продукту який хочете удалити.\n")

    del products[name]

    print("\nПродукт видалено\n")


def show_products():
    for i in products:
        print("Назва продукту: " + i + "\nКількість продукту: " + str(products[i]["count"]) + "\nЦіна продкуту: " + str(products[i]["price"]) + "\n")


def exit():
    sys.exit()


help()

while True:
    answer = input("")

    if answer == "help":
        help()
    elif answer == "add_product":
        add_product()
    elif answer == "delete_product":
        delete_product()
    elif answer == "show_products":
        show_products()
    elif answer == "exit":
        exit()
    elif answer != "":
        print("Такої каманди не існує!")
