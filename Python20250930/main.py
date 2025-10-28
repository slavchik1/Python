with open('data.txt', 'r', encoding='utf-8') as file:
     content = file.read()
     content = content.split(" ")
     print(len(content))