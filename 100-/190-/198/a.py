n = int(input())

count = 0

if n == 0 and n == 1:
    count = 0
elif n == 2:
    count = 1
else:
    n = n-2
    count = n+1
    
print(count)