"""
Assignment:
You've been hired to help a bank automate their deposit/withdrawal system! Your task is to write a Python program that interacts with a customer in order to process a deposit or withdrawal.

Assume the customer has an initial balance of $1000 (you should store the number 1000 in a variable). Then, ask the user two things:

Whether they want to make a deposit or withdrawal

For this step, they should type deposit or withdrawal, depending on what they want to do. It needs to be the exact spelling, including capitalization!
How much money they want to deposit or withdraw

For this step, they should enter an integer.
Then, your program should use an if/elif/else statement to do the following:

If the customer is making a deposit, add the amount to their balance.
If the customer is making a withdrawal, subtract the amount from their balance.
If the customer typed something other than "deposit" or "withdrawal", print "Invalid transaction.".
In this case, the customer's final balance is just the same as their initial balance.
Finally, your program should use an if/else statement to do the following:

If the customer's final balance would be negative (less than zero), tell them "You cannot have a negative balance!".
Otherwise, report their final balance.
"""

# This program simulates a single transaction -
# either a deposit or a withdrawal - at a bank.

initial_balance = 1000 # Sets the initial amount of the user's bank account. 

user_choice = input("Welcome! Would you like to make a deposit or withdrawal? ").lower()
current_balance = initial_balance # Use a new variable for the current balance

if user_choice == "deposit":
    try:
        amount = int(input("How much money would you like to deposit? "))
        if amount > 0: # Check that the deposit amount is positive
            current_balance += amount
            print("Your new balance is:", current_balance)
        else:
            print("Deposit amount must be a positive number.")
            current_balance = initial_balance
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        current_balance = initial_balance

elif user_choice == "withdrawal":
    try:
        amount = int(input("How much money would you like to withdraw? "))
        if amount <= current_balance and amount > 0: # Check if withdrawal is possible
            current_balance -= amount
            print("Your new balance is:", current_balance)
        elif amount <= 0:
            print("Withdrawal amount must be a positive number.")
            current_balance = initial_balance
        else: # Handle insufficient funds
            print("You cannot have a negative balance!")
            current_balance = initial_balance
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        current_balance = initial_balance

else:
    print("Invalid transaction.")
    current_balance = initial_balance

# Final summary
print("Your final balance is:", current_balance)
