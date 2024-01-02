s = list(map(str, input()))

count = []

# 前から一文字ずつ順番にやってくる
for i in range(len(s)-1):
    m = i
    print(11111, i, m)
    series = 0
    for j in range(len(s)-1, -1, -1):
        print(s[m], s[j])
        if s[m] == s[j]:
            m += 1
            series += 1
        if m == len(s):
            break   
    count.append(series)


print(max(count))



# 明日ここから
