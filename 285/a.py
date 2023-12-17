a, b = list(map(int, input().split()))

if a == 1:
    if b == 2 or b == 3:
        print('Yes')
    else:
        print('No')
elif a == 2 or a == 3 or a == 4 or a == 5 or a == 6 or a == 7:
    if b == a*2 or b == a*2+1:
        print('Yes')
    else:
        print('No')
else:
    print('No')
    