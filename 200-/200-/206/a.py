n = int(input())

price = round(1.08 * n)

if price < 206:
    print('Yay!')
elif price == 206:
    print('so-so')
else:
    print(':(')