# 计算BMI, 定义:1. Calculate BMI; 2. Get BMI category; 3. 获取用户输入的体重身高, 打印BMI和类别

def calculate_bmi(weight: float, height: float)->float:
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi)->str:
    if bmi < 18.5:
        return "too thin"
    elif bmi <= 23.9:
        return "normal"
    elif bmi <= 27.9:
        return "overweight"
    else:
        return "obesity"

w = float(input("Enter your weight: "))
h = float(input("Enter your height: "))

b = calculate_bmi(w, h)

category = get_bmi_category(b)
print("Your BMI is", format(b, ".1f"), "and your category is", category)

    
    
