# Password Protection
user_password = input("What is the password? ")
user_password_lowercase = str.lower(user_password)
password = 'secret'

if user_password_lowercase == password:
    print("Welcome!")
else:
    print("Try again!")
