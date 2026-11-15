"""
Assignment:
This program computes how many tons of food each person in a group should take based on how many total tons of food the group has and how many people are in the group. It then asks the user how much food they took.

When you run this program, you'll find that even if you enter what seems to be the correct amount (0.0028), the program will think the amount is incorrect! Fix this program by making it compare rounded versions of the two floats. Round to four decimal places in each case.
"""

# Amount of food and number of people
tons_of_food = 0.07
num_people = 25

# Determine how much food each person gets
tons_of_food_per_person = tons_of_food / num_people

# Ask the user how much food they took
tons_taken = float(input("How many tons of food did you take? "))

# Compare rounded versions of the two floats to four decimal places
if round(tons_taken, 4) == round(tons_of_food_per_person, 4):
    print("Good job, you took the right amount of food!")
else:
    print("You took the wrong amount of food!")
