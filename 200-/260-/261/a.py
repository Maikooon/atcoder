l1, r1, l2, r2 = list(map(int, input().split()))

# 赤で塗られた部分と青で塗られた部分をそれぞれ配列に代入する
red = []
blue = []

for i in range(l1, r1):
    red.append(i)

for i in range(l2, r2):
    blue.append(i)


# 配列も共通要素の個数
same = set(red) & set(blue)

print(len(same))






    