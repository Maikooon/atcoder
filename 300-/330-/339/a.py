s = list(map(str, input().split('.')))

# print(s)
for i in range(len(s)):
    if i == len(s)-1:
        print(s[i])
        break
