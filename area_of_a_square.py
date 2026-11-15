"""
Write a program that will calculate and print the area of a square where its side length is given by the user.

To compute the area, write a function named calculate_area that takes a single parameter, side_length which has a default value of 10. This function should use the side_length parameter to calculate the area of the square (Check out this link to find the formula to calculate the area of a square!)

If the user enters a length value of 0 or less, call calculate_area, use the default value, and write a print statement letting the user know that you are using 10 instead. Otherwise, use the length value given as the parameter value.
"""

import math

# Side length has a default length of 10.
def calculate_area(side_length = 10):
    
   # The formula for the area of a square is side * side
  area = side_length * side_length
  return area

def main():
  try:
    # Gets the user input and converts it into a float  
    user_input = float(input("Enter the side length of the square: "))
    
    # If the user enters value that's greater than or equal to 0, it'll automatically use the default value of 10.
    if user_input <= 0:
      print("The length value entered is 0 or less. Using the default value of 10 instead.")
      area = calculate_area()
      side_used = 10
    else:
    # Calls the function using the user's input as the parameter for side_length
      area = calculate_area(user_input)
      side_used = user_input

    print(f"The area of a square with a side length of {side_used} is: {area}")

    # If the user enters nothing or enters something else other than a number, it will automatically use the default value to calculate the area.
  except ValueError:
    print("Invalid input. Please enter a numerical value.")
    print("Using the default value of 10 instead.")
    area = calculate_area()
    print(f"The area of a square with a side length of 10 is: {area}")

# Function Caller:
if __name__ == "__main__":
  main()
