# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

print("Welcome to the Tip Split Calculator!")


# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

total_cost = input("Please enter the bill amount: $")

total_cost = float(total_cost) 

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

tip_ammount = input("Please enter the tip percent: %")

tip_ammount = float(tip_ammount) 


people_split = input("Please enter how many people in total are splitting the bill: ")

people_split = float(people_split)


total_cost = total_cost * (tip_ammount / 100)

ammount_per_person = total_cost / people_split


print(f"The tip amount each person should leave is ${ammount_per_person} ")


# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!


