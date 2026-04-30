# Name: Estella Cheng
# Date: November 30, 2025
# Class Section: 001
# Assignment 11_Part #2

class Smartphone:
    def __init__(self, capacity, name):
        # total space of phone (integer)
        self.capacity = capacity

        # remaining free space
        self.space_left = capacity

        # name of phone (string)
        self.name = name

        # dictionary to store apps and their sizes
        # key = app name, value = size
        self.apps = {}

        # report
        print("Smartphone created!")
        print("Name:", self.name)
        print("Capacity: 0 out of", self.capacity, "GB")
        print("Available space:", self.space_left)
        print("Apps installed: 0")
        print()

 # --------------------------------------------------

    def add_app(self, appname, appsize):
        # reject if already installed
        if appname in self.apps:
            print("App", appname, "already installed")
            print()
            return

        # reject if no space
        if appsize > self.space_left:
            print("Cannot install app, no available space")
            print()
            return

        # otherwise add app
        self.apps[appname] = appsize
        self.space_left -= appsize
        print()

# --------------------------------------------------
    def remove_app(self, appname):
        if appname not in self.apps:
            print("App", appname, "is not installed")
            print()
            return

        removed_size = self.apps[appname]
        del self.apps[appname]
        self.space_left += removed_size

        print("App removed:", appname)
        print()

 # --------------------------------------------------
    def has_app(self, appname):
        return appname in self.apps

 # --------------------------------------------------

    def get_available_space(self):
        return self.space_left

 # --------------------------------------------------

    def report(self):
        print("Name:", self.name)

        used_space = self.capacity - self.space_left
        print("Capacity:", used_space, "out of", self.capacity, "GB")
        print("Available space:", self.space_left)
        print("Apps installed:", len(self.apps))

        # list apps in alphabetical order
        for app in sorted(self.apps):
            print("*", app, "is using", self.apps[app], "GB")
        print()

 # --------------------------------------------------

# PROGRAM TO TEST THE SMARTPHONE CLASS

while True:
    try:
        cap = int(input("Size of your new smartphone (32, 64 or 128 GB): "))
    except:
        print("Invalid input, please enter a valid number")
    else:
        if cap not in [32, 64, 128]:
            print("Invalid input, please enter 32, 64 or 128")
        else:
            break

name = input("Smartphone name: ")

phone = Smartphone(cap, name)

while True:
    choice = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")

    if choice == "r":
        phone.report()

    elif choice == "a":
        appname = input("App name to add: ")
        while True:
            try:
                appsize = int(input("App size in GB: "))
                if appsize > 0:
                    phone.add_app(appname, appsize)
                    break
                else:
                    print("Invalid input, please enter a valid size")
            except:
                print("Invalid input, please enter a valid size")

    elif choice == "e":
        appname = input("App name to remove: ")
        phone.remove_app(appname)

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
        print()





