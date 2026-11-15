"""
Assignment:
Write a program that asks the user for a number. Report whether that number is positive, zero, or negative. You should use an if-elif-else statement.
"""

try:
    users_number = int(input("Enter a number: ")) # Asks the user for a number.

    # This comparison operator determines if the number is less than 0 (negative number), equal to 0 (neutral), or is greater than 0 (positive number). 
    if users_number < 0:
        print("The number you entered is a negative number.")
    elif users_number == 0:
        print("The number you entered is zero.")
    else:
        print("The number you entered is a positive number.")

except ValueError:
    # If the user doesn't enter a whole number, it prints this error message.
    print("Invalid input. Please enter a whole number.")
