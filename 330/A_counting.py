
all_people, border_line = list(map(int, (input().split())))

# 得点を配列に全て格納
s = list(map(int, input().split()))

total = 0

for i in range(all_people):
    if s[i] >= border_line:
        total += 1

print(total)



