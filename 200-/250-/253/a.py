a, b, c = list(map(int, input().split()))

if a <= b and b <= c:
    print('Yes')
elif c <= b and b <= a:
    print('Yes')
else:
    print('No')