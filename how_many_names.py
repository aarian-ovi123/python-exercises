# Asks the user how many names they have and turns it into an integer.
num_names = int(input("How many names do you have? "))

# This is where the user's full name will be stored as it gets built.
full_name = ""

# This loop asks for each name and adds it to the full name with a space after it.
for name_count in range(num_names):
    name_part = input("Enter a name: ")
    full_name = full_name + name_part + " "

# Prints the full name. strip() removes the extra space left at the end.
print("Your full name is:", full_name.strip())
