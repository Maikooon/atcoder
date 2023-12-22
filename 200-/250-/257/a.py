num, ban = list(map(int, input().split()))

total = []

for i in range(97, 123):
    for j in range(num):
        total.append(chr(i).upper())
        
print(total[ban-1])