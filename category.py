# Let's collect 3 categories with 3 items each
for _ in range(3):
    # Get the category name from user
    category = input("Enter a category: ")
    
    items = []  # store items for this category
   
    # Now get 3 items for this category
    for _ in range(3):
        # Ask for an item in that category
        item = input("Enter something in that category: ")
        items.append(item)
       
    # Print out the category with all its items
    # NOTE: using join to put commas between items - works better than manual concatenation
    print(f"{category}: {', '.join(items)}")
