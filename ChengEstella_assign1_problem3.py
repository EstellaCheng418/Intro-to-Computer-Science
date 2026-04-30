# Name: Estella Cheng
# Date: September 19, 2025
# Class Section: 001
# Assignment 01_Problem #3: Math Expressions

# A list of common conversions
mm_to_in = 0.0394
link_to_in = 7.92
ft_to_in = 12
yd_to_ft = 3
rod_to_link = 25
chain_to_rod = 4
mile_to_yd = 1760

# mm to US Length Units 
mm = 750.0 

# Convert mm to inches
inches = mm * mm_to_in

# Convert inches to other units
links = inches / link_to_in
feet = inches / ft_to_in
yards = feet / yd_to_ft
rods = links / rod_to_link
chains = rods / chain_to_rod
miles = yards / mile_to_yd

# Output
print("-" * 37)
print(" "* 14 + "mm to US Length Units")
print("-" * 37)
print("    mm:" + " "*13, mm)
print("    in:" + " "*14 + "{:.4f}".format(inches))
print("    links:" + " "*10, "{:.9f}".format(links))
print("    ft:" + " "*13, "{:.8f}".format(feet))
print("    yds:" + " "*12, "{:.8f}".format(yards))
print("    rods:" + " "*11, "{:.8f}".format(rods))
print("    chains:" + " "*3, "{:.9f}".format(chains))
print("    mi:" + " "*13, "{:.9f}".format(miles))
print("-" * 37)


