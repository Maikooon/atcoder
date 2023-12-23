a, b = list(map(int, input().split()))

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a_x = 0
a_y = 0
b_x = 0
b_y = 0

# jが同じでIが前後ならおk
for i in range(3):
    for j in range(3):
        if x[i][j] == a:
            a_x = i
            a_y = j

for i in range(3):
    for j in range(3):
        if x[i][j] == b:
            b_x = i
            b_y = j
            
if a_x == b_x and a_y == b_y-1:
    print('Yes')
else:
    print('No')
    
            
            