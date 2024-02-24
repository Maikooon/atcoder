n = int(input())

# n+Nの配列を作る
all = []
for i in range(n):
    sub = [0] * n
    all.append(sub)
# 入力列をAllに代入
for i in range(n):
    a = list(map(int, input()))
    all[i] = a
# print(all)


# まず最も外側に所属する数字を配列に格納する
out = []
# 一番上の段
for i in range(n):
    out.append(all[0][i])
# 右
for i in range(1, n):
    out.append(all[i][n-1])
# 下
for i in range(n-2, -1, -1):
    out.append(all[n-1][i])
# 左
for i in range(n-2, 0, -1):
    out.append(all[i][0])

# 外側のリスト
# print(out)

# 一番外側のリストを変更する
result = all
# for i in range(len(out)):

for j in range(1, n):
    result[0][j] = out[0]
    out.pop(0)
# 右の段
for i in range(1, n):
    result[i][n-1] = out[0]
    out.pop(0)
for i in range(n-2, -1, -1):
    result[n-1][i] = out[0]
    out.pop(0)
for i in range(n-2, -1, -1):
    result[i][0] = out[0]
    out.pop(0)
    
# print(result)
for i in range(n):
    for j in range(n):  
        print(result[i][j], end='') 
    print('')
