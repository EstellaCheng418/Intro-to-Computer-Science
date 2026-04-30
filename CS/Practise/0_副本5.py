# 贷款资格判断, while loop 多次判断
# 输入salary, years, salary > 50,000 & years >= 2 或 salary > 100,000可以获得资格, 每次判断后询问是否继续 yes/no

'''
while True:
    salary = float(input("Enter your salary: "))
    years = int(input("Enter year of working: "))
    if salary > 100000 or (salary > 50000 and years >= 2):
        print("You are eligible.")
    else:
        print("You are not eligible.")

    Decision = input("Do you want to continue: ")
    if Decision == "yes":
        continue
    else:
        break
print("Over")
'''
Decision = "yes"
while Decision == "yes":
    salary = float(input("Enter your salary: "))
    years = int(input("Enter year of working: "))
    if salary > 100000 or (salary > 50000 and years >= 2):
        print("You are eligible.")
    else:
        print("You are not eligible.")

    Decision = input("Do you want to continue: ")
    
print("Over")
