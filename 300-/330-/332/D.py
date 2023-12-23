H, W = list(map(int, input().split()))

a = [input().split() for i in range(H)] 
b = [input().split() for i in range(H)]

count = 0
true = 0

for i in range(H-1):
    for j in range(W-1):
        for row in range(len(a)):
            a[row][j], b[row][j + 1] = b[row][j + 1], a[row][j]
            for i in range(H-1):
                for j in range(W-1):
                    if a[i][j] == b[i][j]:
                        true += 1
    if true == H*W:
        print("Yes")
        break
            
   