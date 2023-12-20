l, r = list(map(int, input().split()))


array = ["a","t","c","o","d","e","r"]

while r - l >= 0:
    print(array[l-1],end="")
    l += 1