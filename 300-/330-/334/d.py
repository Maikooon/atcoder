# 実行時間超過なので無視する
n, q = list(map(int, input().split()))
r = list(map(int, input().split()))


r = sorted(r)
ans = []

# 入力回数分だけループを回す
for i in range(q):
    total = 0
    j = 0
    count = int(input())
    
    for j in range(len(r)):
        count -= r[j]
        if count < 0:
            break
        elif count == 0:
            total += 1
            break
        else:
            total += 1
    ans.append(total)


for i in range(len(ans)):
    print(ans[i])