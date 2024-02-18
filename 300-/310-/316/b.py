m = int(input())
d = list(map(int, input().split()))

total_day = 0
for i in range(len(d)):
    total_day += d[i]

middle = total_day // 2 + 1
# print(middle)

for i in range(len(d)):
    if middle > d[i]:
        middle -= d[i]
    else:
        day = middle
        print(i + 1, day)
        break
