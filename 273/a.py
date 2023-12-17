n = int(input())

first = 0


def func(x):
    if x != 0:
        ans = x * func(x-1)
        return ans
    else:
        return 1


a = func(n)
print(a)