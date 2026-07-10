t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    number = 0
    for i  in range(k - 1):
        if a[i] == 1: number += 1
        else: number += 2 * a[i] - 1
    print(number)

