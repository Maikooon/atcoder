n = int(input())


def six(n):
    flag = 0 
    count = 0
    if n <= 15:
        count += 1
        if n < 10:
            num = n
        elif n == 10:
            num = 'A'
        elif n == 11:
            num = 'B'
        elif n == 12:
            num = 'C'
        elif n == 13:
            num = 'D'
        elif n == 14:
            num = 'E'
        else:
            num = 'F'
        print(num, end='')
    else:
        flag = 1
        
    if flag == 0:
        print('0')
        a = six(n)
        print(a)   
    else:
        sho = n // 16
        six(sho)
        amari = n % 16
        six(amari)

a = six(n)
print(a) 
