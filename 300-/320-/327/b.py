# import math

# b = int(input())

# if b == 1:
#     print(1)
#     exit()
# else:
#     log_b = math.log(b)
#     final = int(18 * math.log(10))
#     for i in range(1, final + 1):
#         if math.isclose(i * math.log(i), log_b):
#             print(i)
#             exit()

# print(-1)

# Aの条件を決めてしまうこと、上限があるので計算できる

B = int(input())

for A in range(1, 16):
    x = 1
    for i in range(A):
        x *= A
    if x == B:
        print(A)
        exit(0)

print(-1)

