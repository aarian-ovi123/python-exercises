# This is the magic number the user has to guess.
my_float = 3.3312

print("Guess the magic float, accurate to within 2 decimal places.")

# This loop keeps asking the user for a guess until they get it right.
while True:
    # Asks the user for a guess and turns it into a float.
    user_guess = input("Enter a guess: ")
    try:
        guess = float(user_guess)
    except ValueError:
        # If the user doesn't enter a number, it prints this message and asks again.
        print("Please enter a number.")
        continue
    
    # Rounds both numbers to 2 decimal places, so the guess only has to be close enough.
    guess_rounded = round(guess, 2)
    target_rounded = round(my_float, 2)
    
    # If the rounded numbers match, the user wins and the loop stops.
    if guess_rounded == target_rounded:
        print("Correct!")
        break
    # If the guess is bigger than the magic number, it tells the user it's too high.
    elif guess > my_float:
        print("Too high!")
    # If it's not correct or too high, it has to be too low.
    else:
        print("Too low!")

print("Game over.")
