a = list(map(int, input().split()))

next = 0

# 中身がわかっていて、インデックスを知りたいとき
for i in range(3):
    # その時のインデックスを取得する
    index = a.index(a[next])
    next = a[index]


print(a[index])
