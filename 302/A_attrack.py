a, b = list(map(int, input().split()))   

count = a//b
lef = a % b

if lef == 0:
    print(count)
else:
    print(count+1)