n = int(input())

a = []
b = []

for i in range(n):
    sub = list(map(int, input().split()))
    a.append(sub)

for i in range(n):
    sub = list(map(int, input().split()))
    b.append(sub)
    
print(a)
print(b)

# まずからの「」を用意
result = []
for i in range(n):
    sub = [0] * n
    result.append(sub)

print(result)


def rotate(result, x, y):
    count_one = 0
    count = 0
    for i in range(n):
        for j in range(n):
            result[i][j] = x[n-1-j][i]
            if result[i][j] == 1:
                count_one += 1
                if y[i][j] != 1:
                    return False
                else:
                    count += 1
    if count_one == count:
        return True


for j in range(n):
    if rotate(result, a, b):
        print('Yes')
        exit()
    else:
        a = result.copy()
        if j == n-1:
            print('No')
        
    

                    
    
            