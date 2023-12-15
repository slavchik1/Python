n = input("Введіть число.\n")
l = "".join([n[i] for i in range(len(n) - 1, -1, -1) if n[i] != "0"])
print(l)
