def checkPassword(password):
    def isspecialsymbol(symbol):
        specialSymbols = "§-=   `./±!@#$%^&*()_+œ∑´´†¥¨ˆˆπ{}'\\./'\"åß∂ƒ©˙∆˚¬…æ«``≈ç√∫˜˜≤≥ç–»јџќ®ёњґѕў‘“ƒыћ÷©}°љ∆…эё]ђ≈≠µи™~≤≥“|~₴Є,/_"

        for i in specialSymbols:
            if symbol == i:
                return True

        return False

    a1 = False
    a2 = False
    a3 = False

    for i in password:
        if i.isdigit():
            a1 = True
    for i in password:
        if i.isupper():
            a2 = True
    for i in password:
        if isspecialsymbol(i):
            a3 = True

    if a1 == True and a2 == True and a3 == True:
        return True
    else:
        return False



print(checkPassword(input("Введіть пароль.\n")))
