from math import gcd
 
t = int(input())
out = []
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    g = gcd(a[0][0], a[n-1][m-1])
    divs = []
    d = 1
    while d * d <= g:
        if g % d == 0:
            divs.append(d)
            if d * d != g:
                divs.append(g // d)
        d += 1
    divs.sort(reverse=True)
    ans = 1
    for D in divs:
        dp = [False] * m
        dp[0] = (a[0][0] % D == 0)
        for j in range(1, m):
            dp[j] = dp[j-1] and (a[0][j] % D == 0)
        if n > 1:
            for i in range(1, n):
                ndp = [False] * m
                ndp[0] = dp[0] and (a[i][0] % D == 0)
                for j in range(1, m):
                    if a[i][j] % D == 0:
                        ndp[j] = dp[j] or ndp[j-1]
                dp = ndp
        if dp[m-1]:
            ans = D
            break
    out.append(str(ans))
print('\n'.join(out))
