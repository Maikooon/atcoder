# TODO 今度やるちょっt無理
a = list(map(int, input().split()))

array = []
count_1 = 0
count_0 = 0
count = 0

for i in range(5):
    if a[i] not in array:
        array.append(a[i])
        count += 1
        if count == 3:
            break
    elif a[i] == array[0]:
        count_0 += 1
    elif a[i] == array[1]:
        count_1 += 1
        
if count == 2 and (count_0 == 2 or count_1 == 2):
    print('Yes')
else:
    print('No')
        
    


    

        
        