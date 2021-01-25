a, b, c, d = map(int, input().split())

# cかdどちらか一方が最大値になるため、単純に計算して最大値を出力すれば良い
print(max(a*c, a*d, b*c, b*d))
