

# できなかった要因
# Lが負の場合は、切り捨ての計算が丸まってしまい、１ずれてしまった
# 場合わけに対応できなかった
# 一歩手前までを考えて引けば、教会の数を考慮する必要がない！


import math
a, m, l, r = list(map(int, input().split()))


count = 0


new_l = l - a
new_r = r - a

print(new_l, new_r)

if new_l == new_r:
    count = 0
elif new_l >= 0:
    start_k = new_l//m
    end_k = new_r//m
    count = end_k - start_k
    if new_l % m == 0 or new_r % m == 0:
        count += 1

    if abs(l - r) % m == 0 and l % m == 0:
        count += 1

else:
    start_k = math.floor(new_l/m)
    if new_l % m != 0:
        start_k += 1

    if new_r >= 0:
        end_k = new_r//m
        count += 1
        count += abs(start_k) + abs(end_k)
    else:
        end_k = math.floor(new_r/m)
        if new_r % m != 0:
            end_k += 1
        count += abs(start_k-end_k)
    if new_l % m == 0 and new_r % m == 0 :
        count += 1 
    print(start_k, end_k)

print(abs(count))





