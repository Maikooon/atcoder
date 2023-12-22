s = list(map(str, input()))

length = len(s)

if length == 1:
    for i in range(6):
        print(s[0], end='')
elif length == 2:
    for i in range(3):
        print(s[0], end='')
        print(s[1], end='')
elif length == 3:
    for i in range(2):
        print(s[0], end='')   
        print(s[1], end='')
        print(s[2], end='') 