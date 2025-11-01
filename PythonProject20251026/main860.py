from typing import List


def lemonadeChange(self, bills: List[int]) -> bool:
    b5 = 0
    b10 = 0

    for b in bills:
        if b == 5:
            b5 += 1
        elif b == 10:
            b5 -= 1
            b10 += 1
        elif b == 20:
            if b10 > 0:
                b10 -= 1
                b5 -= 1
            else:
                b5 -= 3
        if b5 < 0:
            return False
    return True
