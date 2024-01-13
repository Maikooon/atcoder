x = list(map(int, input().split()))

total = 0

for i in range(3):
    total += 7 - x[i]
print(total)