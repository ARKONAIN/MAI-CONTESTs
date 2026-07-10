from math import hypot

N = int(input())
xa, ya, xb, yb = map(int, input().split())
length = hypot(xb - xa, yb - ya)
dp0 = length
dp1 = length
ax, ay, bx, by = xa, ya, xb, yb

for _ in range(N - 1):
    xa, ya, xb, yb = map(int, input().split())
    length = hypot(xb - xa, yb - ya)
    d_a_b = hypot(ax - xb, ay - yb)
    d_b_b = hypot(bx - xb, by - yb)
    new_dp0 = min(dp0 + d_a_b, dp1 + d_b_b) + length
    d_a_a = hypot(ax - xa, ay - ya)
    d_b_a = hypot(bx - xa, by - ya)
    new_dp1 = min(dp0 + d_a_a, dp1 + d_b_a) + length
    dp0, dp1 = new_dp0, new_dp1
    ax, ay, bx, by = xa, ya, xb, yb

print(f"{min(dp0, dp1):.7f}")
