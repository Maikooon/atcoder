s = list(map(str, input()))


new = [''] * 3


new[0] = s[1]
new[1] = s[2]
new[2] = s[0]

for i in range(3):
    print(new[i], end='')



