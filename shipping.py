"""
A quick attempt to better understand how to cast a string into an int, and use if/elif/else
A user can enter an input of weight in lbs to determine their cost for shipping an item

"""


weight = 1
int(input("Please enter your package weight in lbs: "))

# Ground Shipping
if weight <= 2:
    ground_cost = weight * 1.50 + 20.00
elif weight <= 6:
    ground_cost = weight * 3.00 + 20.00
elif weight <= 10:
    ground_cost = weight * 3.00 + 20.00
else:
    ground_cost = weight * 4.75 + 20.00

print("The cost for shipping via ground is: $" + str(ground_cost))

# premium ground shipping
premium_ground_shipping = 125.00

print("The cost for premium shipping is: $" + str(premium_ground_shipping))

# Drone Shipping
if weight <= 2:
    drone_cost = weight * 4.50
elif weight <= 6:
    drone_cost = weight * 9.00
elif weight <= 10:
    drone_cost = weight * 12.00
else:
    drone_cost = weight * 14.25

print("The cost for drone shipping is: $" + str(drone_cost))