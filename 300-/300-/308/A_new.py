s = list(map(int, input().split()))

count = 0

for i in range(len(s)-1):
    if s[i] >= 100 and s[i] <= 675:
        count += 1
    if s[i] % 5 == 0:
        count += 1 
    if s[i] <= s[i+1]:
        count += 1


if count == 3*(len(s)-1):
    print('Yes')
else:
    print('No')
        
