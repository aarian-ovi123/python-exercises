"""
Assignment:
Take your code from the Rectangle exercise in the last lesson, and change it so that the user gets to type the length and width of the rectangle.

As with the exercise in the last lesson, you will need two variables, one called length and one called width. In this exercise, you will need to make a call to input for each of these variables.

Then, write some mathematical expressions in print statements to display the area and perimeter of the rectangle.

An example call for input should look like this:

What is the length?: 10
What is the width?: 5
With the previous values, the following output should be given:

Area: 50
Perimeter: 30
You should be printing a string and a variable on the same line each time.

Tip: You'll need to make use of the int() method.
"""

# Asks the user for values
length = int(input("What is the length?: "))
width = int(input("What is the width?: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Print results using concatenation
print("Area: " + str(area))
print("Perimeter: " + str(perimeter))
