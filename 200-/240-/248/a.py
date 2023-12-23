s = list(map(int, input()))

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(s)):
    if s[i] in array:
        array.remove(s[i])
        
print(array[0])