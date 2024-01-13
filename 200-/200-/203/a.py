a, b, c = list(map(int, input().split()))

if a != b and b != c and c != a:
    print(0)
else:
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)    