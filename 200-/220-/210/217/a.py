s, t = list(map(str, list(map(str, input().split()))))

for i in range(min(len(s), len(t))):
    if ord(s[i]) < ord(t[i]):
        print("Yes")
        exit()
    elif ord(s[i]) > ord(t[i]):
        print("No")
        exit()
    else:
        continue

if len(s) < len(t):
    print("Yes")
else:
    print("No")