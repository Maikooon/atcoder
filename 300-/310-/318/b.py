n = int(input())

x = []
count = 0

for i in range(100):
    y = []
    for j in range(100):
        y.append(0)
    x.append(y)


def print_data():
    for i in range(100):
        for j in range(100):
            print(x[i][j], end=' ')
        print('\n')


for i in range(n):
    a, b, c, d = list(map(int, input().split()))
    for m in range(a, b):
        for n in range(c, d):
            x[m][n] += 1


# print_data()

for i in range(100):
    for j in range(100):
        if x[i][j] > 0:
            count += 1

print(count)
