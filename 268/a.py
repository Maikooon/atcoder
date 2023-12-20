a = list(map(int, input().split()))

count = []

for i in range(len(a)):
    if a[i] not in count:
        count.append(a[i])

print(len(count))