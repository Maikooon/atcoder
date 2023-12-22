year = int(input())


amari = year % 4

# その年に開催される可能性のある時
if amari == 2:
    next = year
# その年には開催され愛とき
elif amari == 0:
    next = year + 2
elif amari == 1:
    next = year + 1
else:
    next = year + 3

print(next)
    
        
        
         
