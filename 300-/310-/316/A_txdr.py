dic = [s for s in str(input())]

array = ''

for i in range(len(dic)):
    if dic[i] != 'a' and dic[i] != 'e' and dic[i] != 'i' and dic[i] != 'o' and dic[i] != 'u':
        array += dic[i]
    
print(array)