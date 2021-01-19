import numpy as np
H, W = map(int, input().split())

# 二次元配列を作成 Hの数だけ繰り返し
A = [list(map(int, input().split())) for i in range(H)]

# npメソッドを使用し、合計値から最小値を引いた値の合計値を算出
A = np.array(A)
print(np.sum(A-np.min(A)))

# numpyメソッドを使用すると、配列同士の計算や配列全体におなじ数を計算するときに便利
