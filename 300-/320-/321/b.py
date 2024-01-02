# どうしてもうまくいかない！！

n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

a = sorted(a)
sub_total = 0
add = 0

if n == 3:
    sub_total += a[0]
    diff = x - sub_total

    if diff > 100:
        add = -1
    elif sub_total >= x:
        add = 0
    elif diff < a[n-2] and diff > a[0]:
        add = diff
    elif diff == a[0]:
        add = 0
    elif diff == a[n-2]:
        add = a[n-2]
    elif diff <= a[0]:
        add = 0
    elif diff >= a[n-2]:
        add = a[n-2]
        
    sub_total += a[1]
    if diff > 100:
        add2 = -1
    elif sub_total >= x:
        add2 = 0
    elif diff < a[n-2] and diff > a[0]:
        add2 = diff
    elif diff == a[0]:
        add2 = 0
    elif diff == a[n-2]:
        add2 = a[n-2]
    elif diff <= a[0]:
        add2 = 0
    elif diff >= a[n-2]:
        add2 = a[n-2]

    
    
else:
    for i in range(1, n-2):
        sub_total += a[i]
    diff = x - sub_total

    if diff > 100:
        add = -1
    elif sub_total >= x:
        add = 0
    elif diff < a[n-2] and diff > a[0]:
        add = diff
    elif diff == a[0]:
        add = 0
    elif diff == a[n-2]:
        add = a[n-2]
    elif diff < a[0]:
        add = 0
    elif diff > a[n-2]:
        add = a[n-2]
        
         
print(add)