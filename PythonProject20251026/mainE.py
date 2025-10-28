INF = 10**100

n = int(input())
b = map(int, input().split())
a = [INF]

for i in b:
    if a[len(a) - 1] > i:
        a[len(a) - 1] = i
    a.append(i)

summ = 0

for i in a:
    summ += i


print (summ)
