a, b = list(map(int, input().split()))

kokei = a + b

if kokei >= 15 and b >= 8:
    print(1)
elif kokei >= 10 and b >= 3:
    print(2)
elif kokei >= 3:
    print(3)
else:
    print(4)
    