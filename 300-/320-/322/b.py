n, m = list(map(int, input().split()))
s = list(map(str, input()))
t = list(map(str, input()))


def head(s, t):
    for i in range(n):
        if s[i] == t[i]:
            continue
        else:
            return False
            break
    return True


def tail(s, t):
    for i in range(n):
        if s[n-i-1] == t[m-i-1]:
            continue
        else:
            return False
            break
    return True


a = head(s, t)
b = tail(s, t)

if a is True and b is True:
    print(0)
elif a is True and b is False:
    print(1)
elif a is False and b is True:
    print(2)
else:
    print(3)
