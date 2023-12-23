n = int(input())


#この方法自分で思いつきたい
def find_all_sums(arr):
    result = set()
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                triplet_sum = arr[i] + arr[j] + arr[k]
                result.add(triplet_sum)

    return sorted(list(result))

#上限が決まっているので、全体から３つを選ぶコートを試せばおk
old_a = []

for i in range(1, 112):
    old_a.append('1'*i)
    
a = [int(s) for s in old_a]
        
all_sums = find_all_sums(a)

print(all_sums[n-1])

