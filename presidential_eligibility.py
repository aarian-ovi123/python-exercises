"""
Assignment:
Write a program that reports whether or not someone is eligible to run for president in the U.S. You should do the following in your program:

Ask the user for their age, and store it in a variable
Ask the user if they are a citizen of the U.S.
Ask the user if they were born in the U.S.
Ask the user how many years they've been a resident of the U.S.

Use an if/else statement with the proper comparison operator to print You are eligible to run for president! if they have the following credentials:

>> They are at least 35 years old
>>> They were born in the U.S.
>>>> They have been a resident for at least 14 years
"""

try:
    # The program first asks for the user's age
    age = int(input("What is your age? "))
    # The program asks if the user is a U.S. citizen
    citizen = input("Are you a citizen of the U.S. (yes/no)? ").strip().lower()
    # The program asks if the user was born in the U.S.
    born_in_us = input("Were you born in the U.S. (yes/no)? ").strip().lower()
    # The program asks for the user's years of residency
    residency = int(input("How many years have you been a resident of the U.S.? "))

    # Initializes a list to store reasons for ineligibility
    reasons = []

    # Checks the age requirement
    if age < 35:
        reasons.append("You are too young. You must be at least 35 years old.")

    # Checks the citizenship requirement
    if citizen != "yes":
        reasons.append("You must be a citizen of the U.S.")

    # Checks the birthplace requirement (the Constitution requires a "natural-born" citizen)
    if born_in_us != "yes":
        reasons.append("You must be a natural-born citizen, born in the U.S.")

    # Checks the residency requirement
    if residency < 14:
        reasons.append("You have not been a resident for long enough. You must have been a resident for at least 14 years.")

    # Outputs the result based on the conditions
    if not reasons:
        print("You are eligible to run for president!")
    else:
        print("You are not eligible to run for president for the following reasons:")
        for reason in reasons:
            print(f"- {reason}")

except ValueError:
    # If the user doesn't enter a whole number for age or residency, it prints this error message.
    print("Invalid input. Please enter your age and years of residency as whole numbers.")
