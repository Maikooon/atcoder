n = int(input())
s = [s for s in str(input())]

isman = 0
iswoman = 0

flag = 0

for i in range(n):
    # 初めにMが来た時
    if s[0] == 'M':
        if s[i] == 'M':
            isman += 1
            if isman != iswoman+1:
                print('No')    
                flag = 1
                break 
        else:
            iswoman += 1
            if iswoman != isman:
                print('No')
                flag = 1
                break
    else:
        if s[i] == 'F':
            iswoman += 1
            if iswoman != isman+1: 
                print('No')  
                flag = 1
                break    
        else:
            isman += 1
            if isman != iswoman:
                print('No')
                flag = 1
                break
        
if flag == 0:
    print('Yes')
