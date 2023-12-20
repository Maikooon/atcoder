today = str(input())

day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(len(day)):
    if today == day[i]:
        print(5 - i)