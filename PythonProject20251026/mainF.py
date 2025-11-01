n = int(input())

A = []

for i in range(n):
    A.append(tuple(map(int, input().split())))

X = {}
Y = {}

for p in A:
    if p[0] not in X:
        X[p[0]] = 0
    if p[1] not in Y:
        Y[p[1]] = 0
    X[p[0]] += 1
    Y[p[1]] += 1

# print(X)
# print(Y)

ans = 0

for i in X:
    if X[i] >= 3:
        ans += X[i] - 2
for i in Y:
    if Y[i] >= 3:
        ans += Y[i] - 2

print(ans)
