num = 0
print(num)
while True:
    choice = input("Command: L, R, or done: ")
    if choice == "L": 
        num = num - 1
        print(num)
    elif choice == "R": 
        num = num + 1
        print(num)
    elif choice == "done":
        break 
    
