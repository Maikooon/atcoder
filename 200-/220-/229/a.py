a = list(map(str, input()))
b = list(map(str, input()))


count = 0

for i in range(2):
    if a[i] == '#':
        count += 1
    if b[i] == '#':
        count += 1
        
# 行き来できない時は、対角線上にある時
if count == 2:
    if a[0] == '#' and b[1] == '#':
        print('No')
    elif a[1] == '#' and b[0] == '#':
        print('No')
    else:
        print('Yes')
else:
    print('Yes')
        