a, b = list(map(int, input().split()))

count = []
array = [1, 2, 3, 4, 5, 6]

for i in range(a):
    for j in range(6):
        count.append( i )
            
print(count)