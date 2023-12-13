s = input("Введіть цілі числа.\n")
s = s.split(" ")
n = [str(int(i)**3) for i in s]
a = ", ".join(n)

print(a)
