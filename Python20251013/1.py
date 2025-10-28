
# Відкрийте файл 'data.txt' в режимі читання з правильним кодуванням
with open('data.txt', 'r', encoding='utf-8') as file:
    # Прочитайте весь вміст файлу в одну змінну
    content = file.read()

    # Розділіть вміст на слова та знайдіть їх кількість
    words = content.split()

    word_count = len(words)

    print(f"Загальна кількість слів у файлі: {word_count}")
