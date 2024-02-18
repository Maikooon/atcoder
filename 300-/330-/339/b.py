#実行時間エラーだがおk
h, w, n = map(int, input().split())

# 文字列はh＊Wの文字列である

now_posx = 0
now_posy = 0
dirc = 90
array = []


# 配列を定義する
for i in range(h):
    row = []
    for j in range(w):
        row.append('.')
    array.append(row)


# 移動する関数を定義
def moveto(dirc, now_posx, now_posy):
    if dirc == 0:
        now_posy = now_posy + 1
        if now_posy == w:
            now_posy = 0
        return now_posx, now_posy
    elif dirc == 90:
        now_posx = now_posx - 1
        if now_posx == h:
            now_posx = 0
        return now_posx, now_posy
    elif dirc == 180:
        now_posy = now_posy - 1
        if now_posy == -1:
            now_posy = w-1
        return now_posx, now_posy
    elif dirc == 270:
        now_posx = now_posx + 1
        if now_posx == h:
            now_posx = 0
        return now_posx, now_posy


def printarray(array):
    for i in array:
        print(''.join(i))


for i in range(n):
    # print('更新前')
    # print(dirc,now_posx, now_posy)
    # 白塗りされている時
    if array[now_posx][now_posy] == '.':
        array[now_posx][now_posy] = '#'
    # すでに黒かった時
        dirc -= 90
        dirc %= 360
        now_posx, now_posy = moveto(dirc, now_posx, now_posy)
    else:
        array[now_posx][now_posy] = '.'
        dirc += 90
        dirc %= 360
        now_posx, now_posy = moveto(dirc, now_posx, now_posy)
        # dirc += 90
        # dirc %= 360
    # print('更新後の座標')
    # print(dirc, now_posx, now_posy)
printarray(array)


# インデックす外れた時の処理がわからん
