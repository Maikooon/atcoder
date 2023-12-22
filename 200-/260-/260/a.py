s = list(input())

same = []
count = 0
flag = 0

# 全て同じ文字の場合を除く
for i in range(len(s)):

    if i > 0 and s[i-1] == s[i]:
        count += 1
        if count == len(s)-1:
            print('-1')
            flag = 1
            break
    if s[i] not in same:
        same.append(s[i])
    elif s[i] in same:
        same.remove(s[i])

if flag == 0:
    print(same[0])

