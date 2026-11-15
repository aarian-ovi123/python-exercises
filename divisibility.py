numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter denominator: "))

# Use a while loop here to repeatedly ask the user for
# a denominator for as long as the denominator is 0
# (or, put another way, until the denominator is not
# equal to 0).

while denominator == 0:
    print("Error: Cannot divide by zero.")
    denominator = int(input("Enter a non-zero denominator: "))

if numerator % denominator == 0:
    print("Divides evenly!")
else:
    print("Doesn't divide evenly.")
