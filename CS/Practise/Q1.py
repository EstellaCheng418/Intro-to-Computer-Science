rate = float(input("How much do you make per hour? "))
hours = float(input("How many hours did you work this week? "))
if hours <= 40:
    pay = rate * hours
    ot_pay = 0                # no overtime pay
else:
    pay = rate * 40
    ot_pay = (hours - 40) * (rate * 1.5)
                 
print("Your total pay is", pay + ot_pay)
       
