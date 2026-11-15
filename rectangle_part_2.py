"""
Assignment:
Alter the Rectangle program you wrote in the last lesson to print out the names of each number being printed. Remember, length is set to 10 and width is set to 5.

Your output should look like this:
Area: 50
Perimeter: 30

Note that you should be using concatenation to print a string and a variable on the same line each time!
"""

# Sets values
length = 10
width = 5

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Print results using concatenation
print("Area: " + str(area))
print("Perimeter: " + str(perimeter))
