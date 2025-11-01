n, m = map(int, input().split())

ops = []
for _ in range(m):
    k, c = map(int, input().split())
    ops.append((c, k))  # зберігаємо як (вартість, кількість)

# сортуємо за спаданням вартості
ops.sort(reverse=True)
print(f"n={n}, m={m}, ops={ops}")
ans = 0
r = n  # скільки ще можемо заповнити
print(f"r={r}")
for c, k in ops:
    take = min(r, k)
    ans += take * c
    r -= take
    print(f"r={r}, k={k}, c={c} => take=min({r}, {k})={take} => ans+({take}*{c})={ans} => r={r}")
    if r == 0:
        break

print(ans)