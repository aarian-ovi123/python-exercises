"""
Assignment:
Write a program that asks the user for their name using input. It should have another string variable that represents the name on a particular table reservation in a restaurant, stored in a variable called reservation_name. The program should print Right this way! if the user's name matches the name on the reservation, and Sorry, we don't have a reservation under that name. otherwise.
"""

users_name = input("What is your name? ") # Asks the user for their name.
reservation_name = "Aarian" # The reservation_name has been only set to one person.

# Uses the if statements to determine if "Aarian" is here. If he is, it'll direct him to his reserved place. If anyone else, it'll print the message in the else branch.
# .strip().lower() makes it so "aarian" or " Aarian " still matches the reservation.
if users_name.strip().lower() == reservation_name.lower():
    print("Right this way!")
else:
    print("Sorry, we don't have a reservation under that name.")
