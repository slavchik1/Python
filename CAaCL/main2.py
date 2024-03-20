def isDividing(a, b):
    if a % b == 0:
        return True
    else:
        return False

print(isDividing(float(input("Введіть перше число.\n")), float(input("Введіть друге число.\n"))))
