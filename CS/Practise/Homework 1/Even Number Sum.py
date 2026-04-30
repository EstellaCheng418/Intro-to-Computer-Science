# Even number sum (1-100)
'''
print("Even numbers between 1 and 100: ")
for i in range(2, 101, 2):
    print(i, end = " ")
total = sum(range(2, 101, 2))
print("\nTotal sum of even numbers:", total)

改成不用sum的, 用一个total每次累加数字的形式。
然后再改一下看看for循环可不可以range(1,101)，用if判断一下是奇数还是偶数（num%2是否等于0）
'''
print("Even numbers between 1 and 100: ")
total = 0 
for i in range(1,101):
    if i % 2 ==0:
        print(i, end = " ")
total += i
print("\nTotal sum of even numbers:", total)


