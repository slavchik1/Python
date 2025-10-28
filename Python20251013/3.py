source_filename = 'source.txt'
destination_filename = 'destination.txt'

try:
    # Використайте вкладені менеджери контексту для одночасної роботи з двома файлами
    with open(source_filename, 'r', encoding='utf-8') as source_file:
        with open(destination_filename, 'w', encoding='utf-8') as dest_file:
            # Прочитайте вміст вихідного файлу
            content = source_file.read()

            # Запишіть цей вміст у файл призначення
            dest_file.write(content)

    print(f"Файл '{source_filename}' було успішно скопійовано в '{destination_filename}'.")

except FileNotFoundError:
    print(f"Помилка: файл '{source_filename}' не знайдено.")

