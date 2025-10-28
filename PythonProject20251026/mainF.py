n = int(input())

A = []

for i in range(n):
    A.append(map(int, input().split()))

for i in range(0, len(A) - 2):
    dx1 = abs(A[i][0] - A[i + 1][0])
    dy1 = abs(A[i][1] - A[i + 1][1])
    
