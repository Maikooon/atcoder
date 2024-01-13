a = list(map(int, input().split()))

# 大きさ順に並べる
a.sort()


if a[2] - a[1] == a[1] - a[0]:
    print("Yes")
else:
    print("No")
    

