N = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if l[i] != l[j] != l[k]:
                if l[i] + l[j] > l[k]:
                    ans += 1
print(ans)
