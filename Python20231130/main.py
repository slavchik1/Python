money = []
categoryes = []
descriptions = []



def help():
    print("""
help - допомога.
add extense - додати витрату.
report - звіт.
report with cetegory - звіт по окремій категорії.""")

def add_extense():
    money.append(input("Введіть суму витрати (₴).\n"))
    answer = input("""Виберіть категорію або дададіть свою витрати, щоб додати свою категорію введіть не цифру, а назву категорії, а якщо вибрать з існуючих то напишіть цифру після назви котегорії, назви категорій та цифра показані нижче.

1 - розваги
2 - продукти
3 - подорожі
""")
    if answer == "1":
        categoryes.append("розваги")
    elif answer == "2":
        categoryes.append("продукти")
    elif answer == "3":
        categoryes.append("подорожі")
    else:
        categoryes.append(input("Введіть категорію.\n"))
    descriptions.append(input("Введіть опис витрати.\n"))

def report():
    for i in range(len(money)):
        print(money[i] + " - " + categoryes[i] + " - " + descriptions[i])

def report_with_cotergory(): #ця функція трошки зламана
    for i in range(len(money)):
        answer = input("Введіть назву котегорії по тільки якій ви хочете отримати звіт.\n")
        if categoryes[i] == answer:
            print(str(money[i]) + " - " + categoryes[i] + " - " + descriptions[i])



help()



while True:
    answer = input()

    if answer == "help":
        help()
    elif answer == "add extense":
        add_extense()
    elif answer == "report":
        report()
    elif answer == "report with cetegory":
        report_with_cotergory()
    elif answer != "":
        print("Такої команди не існує.\n")
