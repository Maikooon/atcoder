n, s, m, l = list(map(int, input().split()))    

# 卵一つあたりの値段を求める
count_6 = n // 6
amari_6 = n % 6
count_8 = n // 8
amari_8 = n % 8 
count_12 = n // 12 
amari_12 = n % 12

price = []

# 想定される変われ方における代金を全て計算して最小値を求める
if n <= 6:
    price.append(s)
    price.append(m)
    price.append(l)
elif n <= 8 and n > 6:
    price.append(m)
    price.append(l)
    price.append(s*2)
elif n <= 12 and n > 8:    
    price.append(l)
    price.append(s*2)
    price.append(m*2)
    price.append(s+m)
else:
    #ひたすら６個を重ねていくパターン
    if amari_6 == 0:
        price.append(count_6 * s)
    else:
        price.append((count_6+1) * s) 
    #ひたすら８こを重ねていくパターン
    if amari_8 == 0:
        price.append(count_8 * m)   
    else:
        price.append((count_8+1) * m)
    #ひたすら１２個を重ねていくパターン
    if amari_12 == 0:
        price.append(count_12 * l)
    else:
        price.append((count_12+1) * l)
        
        price.append(count_12 * l + s)
        price.append(count_12 * l + m)

print(price)
min = min(price)
print(min)
    