N = int(input())

ans = 0
for i in range(N):
    a, b = map(int, input().split())
    # 公式に基づいて計算（整数の和）
    # a - 1の理由はbの時点でaまでの計算をしてるからaの文を省くため
    # 大きい値のBからAをひけば答えを求めることができる
    ans += (b * (b + 1) // 2) - (a * (a - 1) // 2)

print(ans)
