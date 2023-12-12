N = [s for s in input()]


big = N[0]
total = 0

for i in range(len(N)-1):
    if N[i+1] < big:
        big = N[i+1]
        total += 1
        
    else:
        print('No')
        break
    
if total == len(N)-1:
    print('Yes')