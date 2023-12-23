s = list(map(int, input()))

ans = [0, 0, 0, 0]

for i in range(len(s)-1):
    ans[i+1] = s[i]
    
for i in range(len(ans)):
    print(ans[i], end='')