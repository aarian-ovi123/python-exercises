# My magic number - feel free to change this for testing
magic_number = 42

print("Guess the magic number between 1 and 100.")

# Main game loop
while True:
    user_input = input("Enter a guess: ")
    try:
        guess = int(user_input) # converting to integer
    except ValueError:
        print("Please enter a whole number.") # not a number, so ask again
        continue
    
    if guess == magic_number:
        print("Correct!")
        break # we're done!
    elif guess > magic_number:
        print("Too high!")
    else: # must be too low then
        print("Too low!")

print("Game over.")
