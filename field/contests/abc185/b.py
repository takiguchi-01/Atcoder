n, m, t = map(int, input().split())
now = 0
time = n

for i in range(m):
    a, b = map(int, input().split())  # 値取得
    time -= a-now
    if time <= 0:
        print("No")
        exit()
    time += b-a
    time = min(time, n)
    now = b
time -= t-now
if time <= 0:
    print("No")
else:
    print("Yes")
