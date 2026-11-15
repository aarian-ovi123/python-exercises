"""
Assignment:
Write a program that asks the user for the following things:

The names of three ingredients for a salad recipe.
The number of ounces of each ingredient required for one serving (these should just be floats, like 2.5). Make sure to handle the user's input correctly by converting it to a float as you capture it.
The number of servings desired (this should be an integer). You should only ask for the number of servings once. Make sure to handle the user's input correctly by converting it to an int as you capture it.
The program should then output the total number of ounces of each ingredient required to make the desired number of servings.

An example run of your program might look like this:

Enter ingredient 1: mixed greens
Ounces of mixed greens: 1.7
Enter ingredient 2: blueberries
Ounces of blueberries: 2.0
Enter ingredient 3: walnuts
Ounces of walnuts: 0.2
Number of servings: 3

Total ounces of mixed greens: 5.1
Total ounces of blueberries: 6.0
Total ounces of walnuts: 0.6
Note: You must ask the user for an ingredient, and then the amount of that ingredient (as shown in the example above) in order to pass the autograder.
"""

ingredient_one = input("Welcome! Please, proceed with entering the first ingredient for your salad: ") # Asks the user for the first ingredient for the salad.
ingredient_one_quantity = float(input(f"How many ounces of {ingredient_one} do you need? ")) # Asks the user for the amount of ounces they are going to need for the first ingredient.

ingredient_two = input("List the second ingredient for your salad: ") # Asks the user for the second ingredient for the salad.
ingredient_two_quantity = float(input(f"How many ounces of {ingredient_two} do you need? ")) # Asks the user for the amount of ounces they are going to need for the second ingredient.

ingredient_three = input("List the final ingredient for your salad: ") # Asks the user for the final ingredient for the salad.
ingredient_three_quantity = float(input(f"How many ounces are you going to need of {ingredient_three}? ")) # Asks the user for the amount of ounces they are going to need for the final ingredient.

serving_quantity = int(input("How many servings would you like? ")) # Asks the user how many servings they would like of the following ingredients.

# round(..., 2) keeps the totals to 2 decimal places, so 0.2 * 3 shows 0.6 instead of 0.6000000000000001.
ingredient_one_total = round(ingredient_one_quantity * serving_quantity, 2) # Calculates the total ounces for Ingredient One.
print(f"Total ounces for {ingredient_one} is {ingredient_one_total} ounces.") # Prints the total ounces for Ingredient One.

ingredient_two_total = round(ingredient_two_quantity * serving_quantity, 2) # Calculates the total ounces for Ingredient Two.
print(f"Total ounces for {ingredient_two} is {ingredient_two_total} ounces.") # Prints the total ounces for Ingredient Two.

ingredient_three_total = round(ingredient_three_quantity * serving_quantity, 2) # Calculates the total ounces for Ingredient Three.
print(f"Total ounces for {ingredient_three} is {ingredient_three_total} ounces.") # Prints the total ounces for Ingredient Three.
