import math


def solve(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    return x1, x2


print(solve(1, -4, -5))
print(solve(-2, 7, -5))
print(solve(1, 2, 1))
