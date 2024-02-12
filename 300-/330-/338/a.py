s = list(map(str, input()))


flag = 0

for i in range(len(s)):
    if i == 0:
        if s[i].isupper():
            flag += 1
    elif s[i].islower():
        flag += 1


if flag == len(s):
    print('Yes')
else:
    print('No')
