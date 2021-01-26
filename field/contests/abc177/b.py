S = input()
T = input()
len_S = len(S)
len_T = len(T)

ans = len_T


# Tが1文字の時len(S)回、2文字の時len(S) - 1　回なので...
# len(S) - len(T) + 1 で回す
for i in range(len(S) - len(T) + 1):
    num = 0
    for j in range(len(T)):
        if S[i+j] != t[j]
    num += 1
    ans = min(ans, num)

print(ans)
