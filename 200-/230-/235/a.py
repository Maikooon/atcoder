a, b, c = list(map(int, input()))

first = 0 
second = 0
third = 0

first = a * 100 + b * 10 + c
second = b * 100 + c * 10 + a
third = c * 100 + a * 10 + b

ans = first + second + third 
print(ans)