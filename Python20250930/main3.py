with open("1.txt", 'r', encoding='utf-8') as file1:
    with open("2.txt", 'w', encoding='utf-8') as file2:
        file2.write(file1.read())
