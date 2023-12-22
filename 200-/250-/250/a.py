height, width = list(map(int, input().split()))
r, c = list(map(int, input().split()))


# 答えは最小２、最大４
if height == 1 and width == 1:
    print(0)
elif height == 1:
    if c == 1 or width == c:
        print(1)
    else:
        print(2)
elif width == 1:
    if r == 1 or height == r:
        print(1)
    else:
        print(2)
        
elif r == 1 or r == height:
    if c == 1 or c == width:
        print(2)
    else:
        print(3)
else:
    if c == 1 or c == width:
        print(3)
    else:
        print(4)
