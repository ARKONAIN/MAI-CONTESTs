def xor(st, end, cur):
    global maxi
    if end == k:
        maxi = max(maxi, cur)
        return
    for i in range(st, n):
        xor(i + 1, end + 1, cur ^ a[i])
n, k = map(int, input().split())
a = list(map(int, input().split()))
maxi = 0
xor(0, 0, 0)
print(maxi)
 
