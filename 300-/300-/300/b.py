h, w = list(map(int, input().split()))

# 空の二次元配列を作成
a = []
b = []


# def create_list(a):
for i in range(h):
    list = []
    list = list(map(str, input()))
    a.append(list)
for i in range(h):
    list = []
    list = list(map(str, input()))
    b.append(list)


def move_h(num, x):
    new = []
    for i in range(num, h):
        new.append(x[i])
    for i in range(num):
        new.append(x[i])
    # print(new)
    return new


def move_w(num, x):
    y = []
    for m in range(h):
        new = []
        for i in range(num, w):
            new.append(x[m][i])
        for i in range(num):
            new.append(x[m][i])
        y.append(new)
        # print(new)
    return y


# 　縦方向＊横方向を全て確認するk
for i in range(w):
    p = move_w(i, a)
    for j in range(h):
        q = move_h(j, p)
        
        count = 0
        flag = 0
        for s in range(h):
            for t in range(w):
                if q[s][t] == b[s][t]:
                    count += 1
        if count == h*w:
            print('Yes')
            flag += 1
            exit()
if flag == 0:
    print('No')
