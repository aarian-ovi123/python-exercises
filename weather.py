"""
Write a program that will give suggested footwear based on the weather.

Ask the user for the weather outside with three options (sunny, rainy, or snowy) and give the correct footwear suggestion (sandals, galoshes, or boots). Each option should be written as its own function that prints a message based on the input.
"""

# This function will print the type of footwear for sunny weather.
def sunny():
    print("It's sunny! Wear sandals.")
    
# This function will print the type of footwear for rainy weather.
def rainy():
    print("It's rainy! Wear galoshes.")
    
# This function will print the type of footwear for snowy weather.
def snowy():
    print("It's snowy! Wear boots.")
    

# Get input from the user and print matching weather
# If other option, print that it is invalid
weather = input("What's the weather (sunny, rainy, or snowy): ").strip().lower()

if weather == "sunny":
    sunny()
elif weather == "rainy":
    rainy()
elif weather == "snowy":
    snowy()
else:
    print("Invalid option.")
