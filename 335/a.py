s = list(map(str, input()))


s[len(s)-1] = '4'

for i in range(len(s)):
    print(s[i], end='')