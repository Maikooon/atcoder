s = list(map(str, input()))

count = 0

if s[0] == s[1] and s[0] == s[2]:
    count = 1
elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
    count = 3
else:
    count = 6

print(count)