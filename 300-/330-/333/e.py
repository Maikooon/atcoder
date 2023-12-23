n = int(input())

my_list = [[0]*n]*n
leaf = 0
l_list = []

for i in range(n):
    u, v = list(map(int, input().split()))
    my_list[u-1][v-1] = 1
print(my_list)

for i in range(n):
    for j in range(n):
        if my_list[i][j] == 1:
            leaf =+ 1
    if leaf == 1:
        l_list.append(i+1)

for i in range(n):
    if my_list[0][i] == 1 and i 