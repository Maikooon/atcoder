h, w = list(map(int, input().split()))

total = []

# 与えられた文字列をこの順に格納する
for j in range(w):
    sub = list(map(str, input()))
    total.append(sub)

# わかりやすい表示の仕方
for i in range(w):
    print(total[i], end='')
    print('')


for i in range(h):
    for j in range(w):
        # 初めの文字の可能性があるなら
        if total[i][j] == 's':
            if i == 0:
                
# まじでわけわからんので今度やる