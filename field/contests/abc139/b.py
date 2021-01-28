import math
N, D = map(int, input().split())

count = 0
for i in range(N):
    A, B = map(int, input().split())
    C = math.sqrt(A**2 + B**2)
    if D >= C:
        count += 1

print(count)
