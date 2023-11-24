n = int(input("Введіть кількість чисел які ви хочите ввести: "))
l = []
a = 0

for i in range(0, n):
    l.append(int(input("Введіть число: ")))

for i in range(0, n):
    a += l[i]

print(a)
