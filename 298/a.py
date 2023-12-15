n = int(input())
s = [s for s in str(input())]

isgood = 0
isbad = 0
isbetter = 0

for i in range(n):
    if s[i] == 'o':
        isgood += 1
    elif s[i] == 'x':
        isbad = 1
    else:
        isbetter += 1

if isbad == 0 and isgood > 0 and isbetter > 0:
    print('Yes')
elif isgood == n:
    print('Yes')
else:
    print('No')
