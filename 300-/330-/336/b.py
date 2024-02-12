
n = int(input())

a = bin(n)

a_list = list(a)
print(a_list)
count = 0

if a_list[len(a_list)-1] == '1': 
    print(0)
else:
    for i in range(len(a_list)-1, 1, -1):
        if a_list[i] == '1':
            break
        if a_list[i] == '0':
            count += 1
    
    print(count)
            
