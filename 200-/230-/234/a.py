x = int(input())


def calc(f):
    return f**2 + 2*f + 3


ans = calc(calc(calc(x) + x) + calc(calc(x)))
print(ans)
    