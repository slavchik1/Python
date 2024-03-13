n = 3

def factorial(n):
    a = 1
    for i in range(n - 1):
        a *= n - i
    return a

print(factorial(n))
