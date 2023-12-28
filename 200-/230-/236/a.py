s = list(map(str, input()))
a, b = list(map(int, input().split()))


first = s[a-1]
second = s[b-1]

ans = s

ans[a-1] = second
ans[b-1] = first

for i in range(len(ans)):
    print(ans[i], end='')
