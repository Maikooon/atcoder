n = int(input())

result = ''

# 約数を求める
yaku = []
for i in range(1, 10):
    if n % i == 0:
        yaku.append(i)
yaku = sorted(yaku, reverse=False)

# n/jを求める
n_j = []
for i in range(len(yaku)):
    n_j.append(n//yaku[i])
n_j = sorted(n_j, reverse=True)

for i in range(n+1):
    if i == 0:
        result += '1'
    else:
        for j in range(len(yaku)):
            m = i / n_j[j]
            flag = 0
            # print(i, m, n_j[j])
            # もし整数値ならば
            if m.is_integer():
                result += str(yaku[j])
                flag = 1
                break
            if flag == 0 and j == len(yaku)-1:
                result += '-'

print(result)
