"""
Write a function that takes two arguments - a string and an integer - and prints the string multiple times. The integer specifies how many times the string is printed.

In the main part of your program (the part that isn't inside a function), call your function to test it out.
"""

# This function will allow us to take a string and a number.
# Using the for loop, it will loop through using the number of times from the parameter 'number', and print the 'string' that many times.
def print_multiple_times(string, number):
    for i in range(number):
        print(string)

# Testing:
if __name__ == "__main__":
    print_multiple_times("Hello!", 3)
    print_multiple_times("How are you?", 2)
    print_multiple_times("I'm good!", 1)
