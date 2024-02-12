
import sys
n, q = list(map(int, input().split()))

x_pos = 0
y_pos = 0

# 初期位置を持っておく
x_pos_list = []
y_pos_list = [0] * n
for i in range(n):
    x_pos_list.append(i+1)
    
result = []
num = 0

for _ in range(q):
    query = next(sys.stdin)
    p, q = query.split()
    new_xpos = x_pos_list.copy()
    new_ypos = y_pos_list.copy()
    # 移動クエリ
    if p == '1':
        if q == 'R':
            x_pos_list[0] += 1
        elif q == 'L':
            x_pos_list[0] -= 1
        elif q == 'U':
            y_pos_list[0] += 1
        elif q == 'D':
            y_pos_list[0] -= 1
        for m in range(1, n):
            x_pos_list[m] = new_xpos[m-1]
            y_pos_list[m] = new_ypos[m-1]
    # 出力クエリ
    else:
        num += 1
        result.append(x_pos_list[int(q)-1])
        result.append(y_pos_list[int(q)-1])

for i in range(0, len(result), 2):
    print(result[i], result[i+1])
    #実行時間超過