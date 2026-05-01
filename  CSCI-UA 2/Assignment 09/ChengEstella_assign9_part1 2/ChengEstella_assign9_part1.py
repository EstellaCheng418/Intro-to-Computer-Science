# Name: Estella Cheng
# Date: November 14, 2025
# Class Section: 001
# Assignment 09_Part #1: Email Prototype

# ---------- Part 1a ----------

# function:    valid_username
# input:       a username (string)
# processing:  determines if the username supplied is valid. 
#              For the purpose of this program, a valid username is defined as follows:
#              (1) must be 5 characters or longer
#              (2) must be alphanumeric (only letters or numbers)
#              (3) the first character cannot be a number
# output:      boolean (True if valid, False if invalid)

def valid_username(username):
    # (1) length >= 5
    if len(username) < 5:
        return False
    # (2) only letters or numbers
    if not username.isalnum():
        return False
    # (3) first character cannot be a number
    if username[0].isdigit():
        return False
    return True

"""
# valid_username tests
print(valid_username('abc123'))   # True
print(valid_username('abcde'))    # True
print(valid_username('abc'))      # False
print(valid_username('@#$%^'))    # False
print(valid_username('1abcde'))   # False
print(valid_username(''))         # False
"""

# function:    valid_password 
# input:       a password (string)
# processing:  determines if the password supplied is valid. 
#              For the purpose of this program, a valid password is defined as follows:
#              (1) must be 5 characters or longer
#              (2) must be alphanumeric (only letters or numbers)
#              (3) must contain at least one lowercase letter
#              (4) must contain at least one uppercase letter
#              (5) must contain at least one number
# output:      boolean (True if valid, False if invalid)

def valid_password(password):
    # (1) length >= 5
    if len(password) < 5:
        return False
    # (2) only letters or numbers
    if not password.isalnum():
        return False
    # (3) at least one lowercase
    # (4) at least one uppercase
    # (5) at least one number
    has_lower = False
    has_upper = False
    has_digit = False

    i = 0
    while i < len(password):
        ch = password[i]
        if ch.islower():
            has_lower = True
        if ch.isupper():
            has_upper = True
        if ch.isdigit():
            has_digit = True
        i = i + 1

    return has_lower and has_upper and has_digit

"""
# valid_password tests
print(valid_password('Abc123'))        # True
print(valid_password('Abc123xyz'))     # True
print(valid_password('Ab12'))          # False
print(valid_password('abc123'))        # False
print(valid_password('123456'))        # False
print(valid_password('Abc123#'))       # False
print(valid_password(''))              # False
"""

# ---------- Part 1b ----------
# function: username_exists
# input:    a username (string)
# processing:determines if the username exists in the file 'user_info.txt'
# output:   boolean (True if found, False if not found)

def username_exists(username):
    file = open("user_info.txt", "r")
    user_info = file.read()
    file.close()

    parts = user_info.split("\n") # each line is 'username,password'

    for line in parts:
        pieces = line.split(",")  # ['pikachu', 'Abc123']
        if len(pieces) == 2:  # make sure line has username and password
            user = pieces[0]
            if user == username:
                return True

    return False

"""
# username_exists tests
print( username_exists('pikachu') )        # True
print( username_exists('charmander') )     # True
print( username_exists('squirtle') )       # True
print( username_exists('Pidgey2020') )     # True
print( username_exists('SquirtleSquad99') )# False
print( username_exists('eevee') )          # False
print( username_exists('bobcat') )         # False
print( username_exists('') )               # False
"""

# function: check_password
# input:    a username (string) and a password (string)
# processing: determines if the username/password combination 
#           supplied matches one of the user accounts represented
#           in the 'user_info.txt' file 
# output:   boolean (True if valid, False if invalid)

def check_password(username, password):
    file = open("user_info.txt", "r")
    user_info = file.read()
    file.close()

    parts = user_info.split("\n") # each line is 'username,password'

    for line in parts:
        pieces = line.split(",")

        if len(pieces) == 2:
            user = pieces[0]
            user_password = pieces[1]

            if user == username and user_password == password:
                return True
    return False

"""
# check_password tests
print( check_password('pikachu', 'Abc123') )            # True
print( check_password('squirtle', 'SquirtleSquad99') )  # True
print( check_password('fearow', 'Pqr123') )             # False
print( check_password('foobar', 'Hello123') )           # False
print( check_password('', '') )                         # False
"""

# ---------- Part 1c ----------
# function: add_user
# input: a username (string) and a password (string)
# processing: if the user being supplied is not already in the
#             'user_info.txt' file they should be added, along with
#             their password.
# output: boolean (True if added successfully, False if not)

def add_user(username, password):

    # ---- Check if username already exists ----
    file = open("user_info.txt", "r")
    user_info = file.read()
    file.close()

    lines = user_info.split("\n")

    for line in lines:
        pieces = line.split(",")  # ['pikachu', 'Abc123']

        if len(pieces) == 2:      # only process real lines
            user = pieces[0]

            if user == username:  # username already exists
                return False

    # ---- Add new user ----
    file = open("user_info.txt", "a") # append new username and password
    file.write(username + "," + password + "\n")
    file.close()

    # ---- Send welcome message from admin ----
    send_message("admin", username, "Welcome to your account!")

    return True

"""
# add_user tests
add_user('foobar', 'abcABC123')
add_user('barfoo', 'xyz123ABC')
add_user('foobar', 'aTest123') # this should fail
"""

# ---------- Part 1d ----------
# function: send_message
# input:    a sender (string), a recipient (string) and a message (string)
# processing: writes a new line into the specific messages file for the given 
#             users with the following information:
#             sender|date_and_time|message\n
# output: nothing

import datetime
import os

def send_message(sender, recipient, message):
    # make sure folder exists
    if not os.path.exists("messages"):
        os.mkdir("messages")

    # build filename for the recipient
    filename = "messages/" + recipient + ".txt"

    # get current date/time
    d = datetime.datetime.now()
    month = d.month
    day = d.day
    year = d.year
    hour = d.hour
    minute = d.minute
    second = d.second
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    if hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    if second < 10:
        second = "0" + str(second)
    time = str(month) + "/" + str(day) + "/" + str(year) + " " + str(hour) + ":" + str(minute) + ":" + str(second) 

    # open file (append mode)
    file = open(filename, "a")

    # write: sender|date_and_time|message
    file.write(sender + "|" + time + "|" + message + "\n")

    file.close()

"""
# send_message tests
send_message('pikachu', 'charmander', 'Hey there!')
send_message('charmander', 'pikachu', 'Good to see you!')
send_message('pikachu', 'charmander', 'You too, ttyl')
"""

# ---------- Part 1e ----------

# function: print_messages
# input: a username (string)
# processing: prints all messages sent to the username in question.
# output: no return value (simply prints the messages)

def print_messages(username):
    # build the path to this user's message file
    path = "messages/" + username + ".txt"

    # open and read the file
    file = open(path, "r")
    messages = file.read()
    file.close()

    # split into lines
    lines = messages.split("\n")

    count = 1
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line != "":
            parts = line.split("|")   # sender | date_and_time | message
            if len(parts) == 3:
                sender = parts[0]
                when   = parts[1]
                text   = parts[2]

                print("Message #" + str(count) + " received from " + sender)
                print("Time: " + when)
                print(text)
                print()
                count = count + 1
        i = i + 1


# function: delete_messages
# input: a username (string)
# processing: erases all data in the messages file for this user
# output: no return value

def delete_messages(username):
    path = "messages/" + username + ".txt"
    # open in write mode to erase everything
    file = open(path, "w")
    file.close()

# ---------- Part 1f ----------
def main():
    done = False
    while not done:
        print()
        choice = input("(l)ogin, (r)register, or (q)uit: ")

        # ----- quit -----
        if choice == "q":
            print()
            print("Goodbye!")
            done = True

        # ----- register -----
        elif choice == "r":
            print()
            print("Register for am account")
            username = input("Username (case sensitive): ")
            password = input("Password (case sensitive): ")

            # check validity
            if not valid_username(username):
                print("Username is invalid, registration cancelled")
            elif not valid_password(password):
                print("Password is invalid, registration cancelled")
            elif username_exists(username):
                print("Duplicate username, registration cancelled")
            else:
                added = add_user(username, password)
                print("Registration successful!")

        # ----- login -----
        elif choice == "l":
            print()
            print("Log In")
            username = input("Username (case sensitive): ")
            password = input("Password (case sensitive): ")

            logged_in = False
            if check_password(username, password):
                current_user = username
                logged_in = True
            else:
                print("Username or password is incorrect")

            # display menu while the user is logged in
            while logged_in:
                print("You have been logged in successfully as " + current_user)
                action = input("(r)ead messages, (s)end a message, "
                               "(d)elete messages or (l)ogout: ")

                # read messages
                if action == "r":
                    path = "messages/" + current_user + ".txt"
                    f = open(path, "r")
                    contents = f.read()
                    f.close()
                    print()
                    if contents.strip() == "":
                        print("No messages in your inbox")
                        print()
                    else:
                        print_messages(current_user)

                # send a message
                elif action == "s":
                    recipient = input("Username of recipient: ")
                    if not username_exists(recipient):
                        print("Unknown recipient")
                        print()
                    else:
                        text = input("Type your message: ")
                        send_message(current_user, recipient, text)
                        print("Message sent!")
                        print()

                # delete messages
                elif action == "d":
                    delete_messages(current_user)
                    print("Your messages have been deleted")
                    print()

                # logout
                elif action == "l":
                    print("Logging out as username " + current_user)
                    logged_in = False

            

main()










