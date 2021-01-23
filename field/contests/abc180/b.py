import numpy as np

N = int(input())
X = list(map(int, input().split()))

m = 0
e = 0
c = 0

for i in X:  # リストの値を繰り返す
    m += abs(i)  # 絶対値を足す
    e += abs(i) ** 2  # 絶対値を二乗したものを足す
    if c < abs(i):  # 一番大きい値を代入するために条件分岐
        c = abs(i)

print(m)
print(np.sqrt(e))  # 平方根を求める
print(c)
