pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
pi_list = [s for s in pi]


n = int(input())
total = ''

total += pi_list[0]
total += pi_list[1]

for i in range(n):
    total += pi_list[i+2]
    
print(total)
