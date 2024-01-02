n = int(input())

count2 = 0
count3 = 0

# 2と３の掛け算のみで表現できる
while n % 2 == 0:
    count2 += 1
    n = n // 2
    
while n % 3 == 0:
    count3 += 1 
    n = n // 3
    

if n == 1:
    print('Yes')
else:
    print('No')
