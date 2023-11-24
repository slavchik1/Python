def Is_Valid_Triangle(side_1, side_2, side_3):
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        return True
    else:
        return False

print(Is_Valid_Triangle(int(input("Введіть першу сторону.\n")), int(input("Введіть другу сторону.\n")), int(input("Введіть третью сторону.\n"))))
