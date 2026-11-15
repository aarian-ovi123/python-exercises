"""
Write a program that takes a user entered value and adds it to a value taken from the program.

The variable num1 has already been created for you. This should be the only global variable in your program. Don't alter this line of code!

Write a function that gets a second number from the user, adds this number to the user entered value, and prints the result.

Using in-line comments, write the namespace the different variables exist in.
"""

# Global value or namespace:
num1 = 10

# "user_input_str", "num2", and "result" are all local variables or namespace inside this function..
def get_and_add_number():
    try:
        # Asks the user for a number and stores that number into a string.
        user_input_str = input("Enter a number to add to 10: ")
        
        # The number that was stored as a string is then turned into a integer.
        num2 = int(user_input_str)
        
        # Adds the Global Variable and the Local Variable together.
        result = num1 + num2
        
        # Prints the final value.
        print(f"The result of adding {num1} and {num2} is: {result}")
        
    except ValueError:
        # If the user doesn't enter an actual number or enters a float value, it prints this error message.
        print("Invalid input. Please enter a whole number.")

# Calls the function.
get_and_add_number()
