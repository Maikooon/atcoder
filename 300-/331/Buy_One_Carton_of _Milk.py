N, S, M, L = list(map(int, input().split()))
print(N, S, M, L)

#それぞれの卵の一個あたりの値段を求める
S_price = S/6
M_price = M/8
L_price = L/12

if S_price <= M_price:
    if M_price <= L_price:
        high = L_price
        middle = M_price
        low = S_price
    else:
        high = M_price
        middle = L_price
        low = S_price
else:
    if S_price <= L_price:
        high = L_price
        middle = S_price
        low = M_price
    else:
        high = S_price
        middle = L_price
        low = M_price
   

price = 0
total_pack = 0

if N <= 6:
    price = low 
    total_pack = 1
    print(price*total_pack)
elif 6 < N <= 8:
    p
    total_pack = 1
    print(price*total_pack)
    