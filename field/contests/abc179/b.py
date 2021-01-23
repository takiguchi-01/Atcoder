N = int(input())

count = 0
for i in range(N):
    a = list(map(int, input().split()))
    if a[0] == a[1]:
        count += 1
        if count == 3:
            break
    else:
        count = 0

if count >= 3:
    print('Yes')
else:
    print('No')
