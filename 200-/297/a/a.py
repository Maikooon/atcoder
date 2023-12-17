n, d = list(map(int, input().split()))

# クリックが行われた時間
t = list(map(int, input().split()))

flag = 0
for i in range(n-1):
    if t[i+1] - t[i] <= d:
        print(t[i+1])
        break
    else:
        flag += 1

print(flag)

if flag == n-1:
    print('-1')
