a, b, c = list(map(int, input().split()))

thre = b // 100 

double = []
for i in range(1, 1000):
    double.append(i * c)
    

for i in range(thre):
    if double[i] >= a and double[i] <= b:
        print(double[i])
        exit()  
print(-1)