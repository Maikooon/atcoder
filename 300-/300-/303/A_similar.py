length = int(input())
s = [s for s in str(input())]
t = [t for t in str(input())]

flag = 0

for i in range(length):

    if s[i] == t[i]:
        flag += 1 
    elif s[i] == "1" and t[i] == "l":
        flag += 1 
    elif s[i] == "l" and t[i] == "1":
        flag += 1 
    elif s[i] == "0" and t[i] == "o":
        flag += 1 
    elif s[i] == "o" and t[i] == "0": 
        flag += 1
        
if flag == length:
    print('Yes')
else:
    print('No') 