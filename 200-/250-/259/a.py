# TODO  わからんこれ

n, m, x, t, d = list(map(int, input().split()))

height = 0
# 初期値を求める必要があり
init = t - d * x


if m <= x:
    height = init + d*m
else:
    height = t
    
print(height)