array =  list(map(int, input().split()))

result = 0

for i in range(64):
    a = 2 ** i
    result += array[i] * a   
    
    
print(result)