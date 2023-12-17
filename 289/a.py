s = [int(s) for s in input()]

for i in range(len(s)):
    if s[i] == 0:
        s[i] = 1
    elif s[i] == 1:
        s[i] = 0
    print(s[i], end='')
