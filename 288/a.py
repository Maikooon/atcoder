n = int(input())

LIST = []

for i in range(n):
    a, b = list(map(int, input().split()))
    LIST.append(a+b)
    
for i in range(n):
    print(LIST[i])