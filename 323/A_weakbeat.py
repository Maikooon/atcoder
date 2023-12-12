s = [s for s in input()]
total = 0

for i in range(1, 16, 2):
    if s[i] == '0':
        total += 1
    else:
        print('No')
        break  
 
if total == 8:
    print('Yes')