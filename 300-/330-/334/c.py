import math

a, m, l, r = list(map(int, input().split()))

count = 0

new_l = l - a
new_r = r - a

if new_l == new_r:
    count = 0
elif new_l >= 0:
    start_k = new_l // m
    end_k = new_r // m
    count = start_k - end_k
else:
    start_k = math.floor(new_l / m)
    if new_l % m != 0:
        start_k += 1
    if new_r > 0:
        end_k = new_r // m
    else:
        end_k = math.floor(new_r / m)
        if new_r % m != 0:
            end_k += 1
    count = abs(start_k) + abs(end_k)

print(abs(count))
