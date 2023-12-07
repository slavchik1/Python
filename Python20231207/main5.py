n = int(input("Введіть число.\n"))

list = [i ** 2 for i in range(11, n)]

for i in range(len(list)):
    print(list[i])
