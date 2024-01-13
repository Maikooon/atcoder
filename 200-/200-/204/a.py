x, y = list(map(int, input().split()))

array = [0, 1, 2]


if x == y:
    print(x)
else:
    array.remove(x)
    array.remove(y)
    print(array[0])