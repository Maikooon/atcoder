n = int(input())
a = list(map(int, input().split()))

count = 0
i = 0

# 間が１のみだったとき
while len(a)-1 > i:
    # print(a[i], a[i+1])
    if abs(a[i] - a[i+1]) == 1:
        count += 1
        i += 1
    elif a[i] < a[i+1]:
        # 次の項においくつまで、項を追加していく
        while a[i] < a[i+1]-1:
            a.insert(i+1, a[i] + 1)
            i += 1
    elif a[i] > a[i+1]:
        # 次の項においくつまで、項を追加していく
        while a[i]-1 > a[i+1]:
            a.insert(i+1, a[i] - 1)
            i += 1

           
for i in range(len(a)):
    print(a[i], end=' ')

    