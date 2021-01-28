s = input()

count = 0
for i in range(len(s) // 2):  # 半分まで判定する。
    if s[i] != s[len(s) - i - 1]:  # 反対側から比較していく -1は調整
        count += 1
print(count)
