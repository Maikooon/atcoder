a, b = list(map(int, input().split()))

if a == b:
    print(1)
else:
    print(32 ** (a-b))