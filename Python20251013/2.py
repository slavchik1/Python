numbers = [1, 5, 8, 12, 15, 20, 22, 27]

# Відкрийте файл 'even_numbers.txt' в режимі запису ('w')
with open('even_numbers.txt', 'w', encoding='utf-8') as file:
    # Пройдіться по списку чисел
    for num in numbers:
        # Перевірте, чи є число парним
        if num % 2 == 0:
            # Запишіть число у файл, не забуваючи додати символ нового рядка '\n'
            file.write(f"{num}\n")

print("Парні числа було успішно записано у файл.")