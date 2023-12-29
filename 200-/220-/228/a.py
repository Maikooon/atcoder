s, t, x = list(map(int, input().split()))

if s < t:
    if s <= x and x < t:
        print('Yes')
    else:
        print('No')
elif s == t:
    print('No')
else:
    # 日つけが変わる時
    if (s <= x and x <= 23) or (0 <= x and x < t):
        print('Yes')
    else:
        print('No')
    
