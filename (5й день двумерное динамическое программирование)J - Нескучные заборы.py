modul = 10**9 + 7
n = int(input())
sp = [0] * (n + 1)
sp[0] = 1
for x in range(1, n + 1):
    for s in range(n, x - 1, -1):
        sp[s] = (sp[s] + sp[s - x]) % modul
print(sp[n])
