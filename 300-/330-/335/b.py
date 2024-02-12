n = int(input())

list = []

# while True:
for i in range(22):
    for j in range(22):
        for m in range(22):
            total = 0
            total = i + j + m
            if total <= n:
                list.append(total)
                print(i, j, m)


