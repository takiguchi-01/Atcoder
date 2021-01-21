N, X = map(int, input().split())
S = list(input())

count = 0
for i in range(N):
    if S[i] == 'o':
        count += 1
    else:
        count -= 1

if X + count >= 0:
    print(X + count)
else:
    print(0)
