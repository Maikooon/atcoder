n = int(input())



if n <= 10**3 - 1:
    print(n)
elif n >= 10**3 and n <= 10**4-1:
    print(n//(10**1), end='')
    print('0')

elif n >= 10**4 and n <= 10**5-1:
    print(n//(10**2), end='')
    print('00')

elif n >= 10**5 and n <= 10**6-1:
    print(n//(10**3), end='')
    print('000')

elif n >= 10**6 and n <= 10**7-1:
    print(n//(10**4), end='')
    print('0000')

elif n >= 10**7 and n <= 10**8-1:
    print(n//(10**5), end='')
    print('00000') 

elif n >= 10**8 and n <= 10**9-1:
    print(n//(10**6), end='')
    print('000000')
