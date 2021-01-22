N = int(input())
A = list(map(int, input().split()))

ans = 0
mx = 0

for x in range(2, 1001):
    s = sum(i % x == 0 for i in A)
    if mx < s:
        mx = s
        ans = x

print(ans)
