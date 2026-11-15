"""
Assignment:
Your friend is about to have a birthday! Write a program that asks them how old they are. Once they enter their age, print how many candles they'll need for their birthday cake. (This should be one more than their current age.)

You will have to create a variable called age and use the input function to retrieve information from the user. Also, you should use the int function to convert what they type into an integer. Finally, you'll have to alter their age variable to tell the user how many candles they will need.
"""

age = int(input("How old are you? ")) #Asks the user how old they are.
age = age + 1 #Adds one to their age to determine how many candles they'll need.
print("You're going to need this many candles for your birthday cake!") #Informs them how many candles they'll need.
print(age) #End result.
