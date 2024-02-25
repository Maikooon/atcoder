n, m = list(map(int, input().split()))

# 全ての組み合わせを持つリストを作成し、そこにチェックを入れていく
all = []


for i in range(n):
    sub = []
    for j in range(n):
        if i == j:
            sub.append(9)
        else:
            sub.append(0)
    all.append(sub)
# print(all)


# となりあう列を読み込む
for i in range(m):
    a = list(map(int, input().split()))
    for i in range(n-1):
        # print(all[a[i]-1][a[i+1]-1])
        # print(all[a[i+1]-1][a[i]-1])
        all[a[i]-1][a[i+1]-1] = 1
        all[a[i+1]-1][a[i]-1] = 1

# print(all)

# ０であるペアを探してその数をカウントする
count = 0
for i in range(n):
    for j in range(n):
        if all[i][j] == 0:
            count += 1

print(count//2)

