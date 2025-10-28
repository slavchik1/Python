file_name = "users.log"

try:
    with open(file_name, 'r') as content:
        with open(file_name, 'a') as where_to_write:
            where_to_write.write(f"Ім'я: {input("Введіть ваше ім'я: ")}, Вік: {input("Введіть ваш вік: ")}\n")
    with open(file_name, "r",) as new_content:
        print("Дані успішно додано. Вміст журналу:\n" + new_content.read())
except:
    print(f"Помилка: файл '{file_name}' не знайдено.")