
s = list(map(int, input().split()))

period_month = s[0]
period_day = s[1]


t = list(map(int, input().split()))
year = t[0]
month = t[1]
day = t[2]


if day == period_day:
    day = 1
    if month == period_month:
        month = 1
        year += 1
    else:
        month += 1 
else:
    day += 1
    
    
print(year, month, day)
  
