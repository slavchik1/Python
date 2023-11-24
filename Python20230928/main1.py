a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третье число: "))

if b != a + (b - a):
    print("NO")
elif c != b + (b - a):
    print("NO")
else:
    print("YES")
