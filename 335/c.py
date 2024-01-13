import copy
n, q = list(map(int, input().split()))

x_pos = 0
y_pos = 0

# 初期位置を持っておく
x_pos_list = []
y_pos_list = [0] * n
for i in range(n):
    x_pos_list.append(i+1)
    
new_xpos = x_pos_list.copy()
new_ypos = y_pos_list.copy()

print(new_xpos)

num = 0

for i in range(q):
    p, q = list(map(str, input().split()))
    # 移動クエリ
    if p == '1':
        num += 1
        if q == 'R':
            x_pos_list[num-1] += 1
        elif q == 'L':
            x_pos_list[num-1] -= 1
        elif q == 'U':
            y_pos_list[num-1] += 1
        elif q == 'D':
            y_pos_list[num-1] -= 1
        # 動くたびにそれ以外の座標の値が更新される
        for m in range(num, n):
            print(m)
            x_pos_list[m] = new_xpos[m-1]
            y_pos_list[m] = new_ypos[m-1]
            print(x_pos_list)
            print(y_pos_list)

    # 出力クエリ
    else:
        print(x_pos_list[int(q)-1], y_pos_list[int(q)-1])
    print(x_pos_list)
    print(y_pos_list)