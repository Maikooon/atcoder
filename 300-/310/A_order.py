n, p, q = list(map(int, input().split()))
d = list(map(int, input().split()))

min = min(d)


if q+min > p:
    print(p)
else:
    print(q+min)

