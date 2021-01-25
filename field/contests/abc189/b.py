N, X = map(int, input().split())
alc = 0

for i in range(N):
    V, P = map(int, input().split())

    # そのまま割り算で計算すると小数点のため、誤差が生まれる
    # そのため分けてかけることによって回避している
    alc += V * P
    if alc > X * 100:
        print(i+1)
        exit()

print(-1)
