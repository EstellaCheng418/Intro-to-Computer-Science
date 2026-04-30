# 多次购物，用户如果输入原价>100, 打九折;小于=100， 不打折；每次计算后询问是否继续，yes/no

total = 0
Decision = "yes"

while Decision == "yes":
    price = float(input("Enter price: "))
    if price > 100:
        price = price * 0.9
    else:
        price = price
    total += price 
    
    Decision = input("Do you want to continue: ")

print("Total price is", total)
