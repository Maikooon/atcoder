# 異なったら０、同じだったら１を出力する
# 全て２進数表記にしてから、上の逆を実行する

a, b = list(map(int, input().split()))
two_a = bin(a)
two_b = bin(b)

max_len = max(len(two_a), len(two_b))
two_a = two_a.zfill(max_len)
two_b = two_b.zfill(max_len)

c = []
print(two_a)
print(two_b)


for i in range(max(len(two_a), len(two_b)-1), 0, -1):
    print(i)
    if ((two_a[i] == 1 and two_b[i] == 0) or (two_a[i] == 0 and two_a[i] == 1)):
        c.append = 1
        print(c)
    else:
        c.append = 0
    #     c[i] = 1
    # else:
    #     c[i] = 0
print(c)


# try agrain!!!!!!!!!!!!!!!
