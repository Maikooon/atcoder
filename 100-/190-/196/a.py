a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))


# 正負で場合分けを行う
if a >= 0:
    if c >= 0:
        result = b - c
    elif c < 0:
        result = b - c
elif a < 0 and b > 0:
    if c >= 0:
        result = b - c
    elif c < 0:
        result = b - c

elif b <= 0:
    if c >= 0:
        result = b - c
    elif c < 0 and d > 0:
        result = b - c
    else:
        result = b - c
        
print(result)