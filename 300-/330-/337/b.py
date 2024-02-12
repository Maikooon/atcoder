s = list(map(str, input()))

flag_a = 0
flag_b = 0
flag_c = 0

#初めに全てのアルファベットの出現頻度を調べる
count_a = s.count('A')
count_b = s.count('B')
count_c = s.count('C')

# print(count_a, count_b, count_c)
result = []
 
        
for i in range(count_a):
    result.append('A')
for i in range(count_b):
    result.append('B')
for i in range(count_c):
    result.append('C')
        
if s == result:
    print('Yes')
else:
    print('No')
    