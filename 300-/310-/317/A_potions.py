n, h, x = list(map(int, input().split()))
p = list(map(int, input().split()))


array = []
total = h
thre = 0
small = 0


for i in range(n):
    a = total + p[i]
    array.append(a)


print(array)

for i in range(n):
    if array[i] > x:
        if array[i] < small:
            small = array[i]
            number = i
            print(small)
            print(number)
        