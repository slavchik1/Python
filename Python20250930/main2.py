numbers = [747, 6278, 3467, 256, 45678, 46]

with open('data2.txt', 'w', encoding='utf-8') as file:
    for num in numbers:
        if num % 2 == 0:
            file.write(str(num) + '\n')
