n, k, a = list(map(int, input().split()))

amari = k % n


# Aから始めたK番目は何でしょうかということ
for i in range(a, n+a-1):
    if (amari == 0 and i == a):
        if (a > 1):
            print(a-1)
        else:
            print(n)
        exit()
    else:
        amari -= 1
        if amari == 0:
            if i <= n:
                print(i)
            else:
                print(i-a-1)   
        
