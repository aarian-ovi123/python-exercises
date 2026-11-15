# This program calculates the average of 3 test scores.

# This is where the scores will be added together.
total = 0

# This loop asks the user for 3 test scores and adds each one to the total.
for count in range(3):
    score = int(input("Enter test score: "))
    total = total + score

# Divides the total by 3.0 so the average can have decimals.
avg = total / 3.0

# Prints the average score.
print("Average Score: " + str(avg))
