def is_palindrome(text):
    return_variable = True
    ftext = ""

    for i in range(len(text)):
        if text[i] != " " and text[i] != "," and text[i] != "." and text[i] != "," and text[i] != "!" and text[i] != "?" and text[i] != "-":
            ftext += text[i]

    ftext = ftext.lower()

    for i in range(len(ftext) // 2):
        if ftext[i] != ftext[len(ftext) - i - 1]:
            return_variable = False

    return return_variable


print(is_palindrome("А роза упала на лапуАзора."))
print(is_palindrome("Gabler Ruby - burrel bag!"))
print(is_palindrome("BEEGEEK"))
