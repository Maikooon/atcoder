n = int(input())

like = []

for i in range(1, 10):
    for j in range(0, 10):
        if i * j <= 9:
            like.append(100*i+10*j+i*j)
            

count = 0

for i in range(len(like)):
    if like[i] >= n:
        print(like[i])
        exit()