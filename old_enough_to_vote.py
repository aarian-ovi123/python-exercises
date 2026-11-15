"""
Assignment:
Write a program that reports whether or not someone is old enough to vote in the U.S. You should do the following in your program:

Ask the user for their age, and store it in a variable
Use an if/else statement with the proper comparison operator to print You are old enough to vote! if the person's age is at least 18, and You are not old enough to vote. otherwise.
"""

try:
    age = int(input("How old are you? ")) # Asks the user how old they are.

    if age >= 18: # Uses a comparison operator to determine if the user is old enough to vote.
        print("You are old enough to vote!")
    else:
        print("You are not old enough to vote, yet!")

except ValueError:
    # If the user doesn't enter a whole number, it prints this error message.
    print("Invalid input. Please enter your age as a whole number.")
