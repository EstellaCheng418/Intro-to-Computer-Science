# while loop, calculate average from 1 to n (user input)

n = int(input("Enter an integer: "))
# total = 0
# count = 0
'''
for i in range(1, n + 1):
    total += i
    count += 1

average = total / count
'''
'''
i = 1
while i <= n:
    total += i
    count += 1
    i += 1
'''
'''
for i in range(1, n + 1):
    total *= i
'''
'''
total = 1
i = 1
while i <= n:
    total *= i
    i += 1
'''
'''
# 1-100 累加奇数
total = 0
for i in range(1, 101):
    if i % 2 == 1:
        total += i
'''
i = 0
total = 0
while i <= n:
    if i % 2 == 1:
        total += i
    i += 1
print(total)
    
