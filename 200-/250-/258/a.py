min = int(input())

if min < 60:
    if min < 10:
        print('21:0{min}'.format(min=min))
    else:
        print('21:{min}'.format(min=min))
        

else:
    new_min = min - 60 
    if new_min < 10:
        print('22:0{min}'.format(min=new_min))
    else:
        print('22:{min}'.format(min=new_min))