# Let's generate all possible combinations when rolling two dice
for first_die in range(1, 7):    # first die can be 1-6
    for second_die in range(1, 7):  # second die can also be 1-6
        # Output each combo - keeping it simple with comma separation
        print(f"{first_die},{second_die}")
