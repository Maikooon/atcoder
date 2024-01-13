v, s, t, d = list(map(int, input().split()))

now = d / v


if s <= now and t >= now:
    print('No')
else:
    print('Yes')