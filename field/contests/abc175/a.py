s = input()
cnt = 0
ans = 0
for i in range(3):
    if s[i] == 'R':
        cnt += 1
        if cnt >= ans:
            ans = cnt
    else:
        cnt = 0
print(ans)
