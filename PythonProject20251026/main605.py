from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    c = len(flowerbed)
    deleted = {}
    not_free = []
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            pass
        else:
            not_free.append(i)
            if i - 1 >= 0:
                if flowerbed[i - 1] == 0 and i - 1 not in deleted:
                    not_free.append(i - 1)
            if i + 1 <= len(flowerbed) - 1:
                if flowerbed[i + 1] == 0:
                    deleted[i + 1] = True
                    not_free.append(i + 1)
    not_free.sort()
    not_free2 = [-1] * len(flowerbed)
    for i in not_free:
        not_free2[i] = i
    free = []
    for i in range(len(not_free2)):
        if not_free2[i] == -1:
            free.append(i)
    i = 0
    while i < len(free) - 1:
        if free[i + 1] == free[i] + 1:
            free.pop(i + 1)
            i += 1
        i += 1
    if len(free) >= n:
        return True
    else:
        return False




print(canPlaceFlowers([0,0,0,0], 3))
