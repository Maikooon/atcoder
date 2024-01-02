n = int(input())

score = [0] * n


for i in range(1, n+1):
    array = []
    array = list(map(str, input()))
    for j in range(n):
        if array[j] == 'x':
            score[j] += 1


# print(score)

my_dict = {index: value for index, value in enumerate(score)}
my_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
sorted_key = list(my_dict.keys())
# print(my_dict)
# print(sorted_key)

for i in range(n):
    print(sorted_key[i] + 1, end=' ')
    


