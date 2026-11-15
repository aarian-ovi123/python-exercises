"""
Write a function that takes two arguments, both integers, and prints the product.

In the main part of your program (the part that isn't inside a function), call your function to test it out.
"""

# This function will allow us to take two numbers and input them into our parameters, allowing for them to print a product.
def print_product(num1, num2):
  product = num1 * num2
  print(f"The product of {num1} and {num2} is: {product}")

# Main part of the program:
if __name__ == "__main__":
  # Call the function to test it out
  print_product(5, 10) # Output: The product of 5 and 10 is: 50
  print_product(-3, 7) # Output: The product of -3 and 7 is: -21
  print_product(0, 99) # Output: The product of 0 and 99 is: 0
