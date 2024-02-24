n, m = list(map(int, input().split()))

color = []
color_list = []
price_list = []
total_price = 0

color = list(map(str, input().split()))
color_list = list(map(str, input().split()))
price_list = list(map(int, input().split()))

dict = {}
p0 = price_list[0]
price_list.pop(0)

# print(color_list)
# print(price_list)

for i in range(m):
    dict[color_list[i]] = price_list[i]
# print(dict)

for i in range(n):
    if color[i] in color_list:
        total_price += dict[color[i]]
    else:
        total_price += p0   
print(total_price)



