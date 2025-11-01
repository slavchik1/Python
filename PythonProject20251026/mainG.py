n, m = map(int, input().split())

O = []
summ = 0

for _ in range(m):
    O.append(list(map(int, input().split())))

O.sort(key=lambda x: x[1], reverse=True)

r = n
i = 0

while r >= 0 and i < len(O):
    k = O[i][0]
    c = O[i][1]
    summ += c * min(k, r)
    i += 1
    r -= k

print(summ)
