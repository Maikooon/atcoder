# 実行時間超過だが答えはおk
n, l, r = list(map(int, input().split()))

a = list(map(int, input().split()))
array = []

for i in range(len(a)):
    for j in range(l, r+1):
        array.append(abs(a[i] - j))
    small = min(array)
    ans = small + a[i]
    if (ans < l or ans > r):
        if ans < l:
            ans = l
        elif ans > r:
            ans = r

    print(ans, end=' ')