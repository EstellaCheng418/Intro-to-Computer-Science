# Name: Estella Cheng
# Date: December 4, 2025
# Class Section: 001
# Assignment 11_Part #1: Gumball Machine

import random
class Gumball_Machine:
    def __init__(self, capacity):
        # store capacity
        self.capacity = capacity

        # store money (starts at 0)
        self.money = 0.00

        # make list of random gumballs
        colors = ["red", "green", "blue"]
        self.gumballs = []

        for i in range(self.capacity):
            rand_color = random.choice(colors)
            self.gumballs.append(rand_color)

        # announce
        print("Gumball Machine created with", self.capacity, "random gumballs")
        print()

# -------------------------------------------------

    def report(self):
        print("Gumball Machine Report:")
        print("* Gumballs in machine:", len(self.gumballs))
        print("* Money in machine: $" + format(self.money, ".2f"))
        print()

 # -------------------------------------------------
    def dispense(self, coin):
        # only accept 0.25
        if coin != 0.25:
            print("Invalid coin, no gumball will be dispensed")
            print()
            return

        # machine empty
        if len(self.gumballs) == 0:
            print("Machine is empty, no gumball will be dispensed")
            print()
            return

        # otherwise accept coin and randomly dispense one gumball
        # choose a random index, then remove that gumball
        rand_index = random.randint(0, len(self.gumballs) - 1)
        color = self.gumballs[rand_index]
        del self.gumballs[rand_index]
        self.money += coin

        print("Accepting " + str(coin) + "; Dispensing a", color, "gumball")
        print()

# -------------------------------------------------

    def count_gumballs_by_type(self, color):
        if color not in ["red", "green", "blue"]:
            print("Invalid color, no gumballs will be counted")
            print()
            return

        count = 0
        for g in self.gumballs:
            if g == color:
                count += 1

        print("There are", count, "gumballs of type", color, "in the machine")
        print()


# TESTER CODE

machine = Gumball_Machine(5)
machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")






















