a, b = list(map(int, input().split()))

ans = []

for i in range(5):
    if i == 0:
        ans.append(b//a)
        ans.append('.')
    elif i == 4:
        left = b % a
        b = 10*left
        if b//a >= 5:
            ans[4] += 1
    else:
        left = b % a
        b = 10*left
        ans.append(b//a)

for i in range(len(ans)):
    print(ans[i], end="")
