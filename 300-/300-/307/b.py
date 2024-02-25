n = int(input())

total = []
tag = 0

for i in range(n):
    s = list(map(str, input()))
    total.append(s)
# print(total)


# 前から順に組み合わせを考える
for i in range(n-1):
    for j in range(i+1, n):
        # print(total[i], total[j])
        isround = []
        isround += total[i]
        isround += total[j]
        # print(isround)

        # ここで回文か否かのチェックを行う
        count = 0
        # print(len(isround))
        for p in range(len(isround)//2):
            # print(isround[p], isround[len(isround)-1-p])
            if isround[p] == isround[len(isround)-1-p]:
                count += 1
            #     count += 1
            # tag = 1
            # break
        # print(count)
        if count == len(isround)//2:
            tag = 1
            # print('Yes')
            break 

for i in range(n-1):
    for j in range(i+1, n):
        # print(total[i], total[j])
        isround = []
        isround += total[j]
        isround += total[]
        # print(isround)

        # ここで回文か否かのチェックを行う
        count = 0
        # print(len(isround))
        for p in range(len(isround)//2):
            # print(isround[p], isround[len(isround)-1-p])
            if isround[p] == isround[len(isround)-1-p]:
                count += 1
            #     count += 1
            # tag = 1
            # break
        # print(count)
        if count == len(isround)//2:
            tag = 1
            # print('Yes')
            break 

# ここで反対側亞かrあのチェックを繰り返す


if tag == 1:
    print('Yes')
else:
    print('No')
