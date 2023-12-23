a_time, b, c_sec, b_time, e, f_sec, x = list(map(int, input().split()))


def takahashi(sec):
    term = a_time + c_sec
    syo = x // term 
    amari = x % term
    total = a_time * b * syo
    if amari <= a_time:
        total += amari * b 
    else:
        total += a_time * b
    return total


def aono(sec):
    term = b_time + f_sec
    syo = x // term 
    amari = x % term
    total = b_time * e * syo
    if amari <= b_time:
        total += amari * e
    else:
        total += b_time * e
    return total


if takahashi(x) > aono(x):
    print('Takahashi')
elif takahashi(x) < aono(x):
    print('Aoki')
else:
    print('Draw')
    
