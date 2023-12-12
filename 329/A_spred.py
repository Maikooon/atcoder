s = [s for s in input()]
print(s)

for i in range(len(s)):
    if i == len(s) - 1:
        print(s[i])
    else:
        print(s[i], end=" ")
    