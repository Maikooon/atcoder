n = int(input())
d = list(map(int, input().split()))

count = 0

for i in range(1, n + 1):
    # print(i, '月のごろめ')
    j = 0
    now = i
    if i < 10:
        while now <= d[i - 1]:
            if j == 0:
                # 一桁のときの処理
                count += 1
                j += 1

            else:
                if i*(10**j) + now <= d[i - 1]:
                    now = i*(10**j) + now
                    count += 1
                    j += 1
                else:
                    break
            # print(now) 
    elif i >= 10 and i <= 100:
        syo = i // 10
        amari = i % 10
        now = amari
        if syo == amari: 
            while now <= d[i - 1]:
                if j == 0:
                    # 一桁のときの処理
                    count += 1
                    j += 1
                else:
                    if amari*(10**j) + now <= d[i - 1]:
                        now = amari*(10**j) + now
                        count += 1
                        j += 1
                    else:
                        break


print(count)
