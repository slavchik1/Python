with open("numbers.txt", "r", encoding='utf-8') as file:
    numbers = file.read().split("\n")
    summ = 0
    for i in numbers:
        summ += float(i)
    with open("sum.txt", 'w') as summm:
        summm.write(str(summ))
