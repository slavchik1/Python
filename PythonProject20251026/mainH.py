n, m, k = map(int, input().split())
P = []
for _ in range(k):
    P.append(tuple(map(int, input().split())))

ans = set()

# Захід №1, по x-ах

y0 = 1
for x in range(1, n + 1):
    if (x, y0) in P:
        break
    ans.add((x, y0))
    for y in range(1, m + 1):
        if (x, y) in P:
            break
        ans.add((x, y))

x0 = 1
for y in range(1, m + 1):
    if (x0, y) in P:
        break
    ans.add((x0, y))
    for x in range(1, n + 1):
        if (x, y) in P:
            break
        ans.add((x, y))


#print(ans)
print(len(ans) - 1)
