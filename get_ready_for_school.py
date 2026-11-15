# Each function below prints one step of my morning routine before school.

def wake_up():
    # Prints the first step of the day.
    print("Waking up...")

def brush_teeth(duration = 120):
    # Brushing takes 120 seconds unless a different time is given.
    print(f"Brushing teeth for {duration} seconds...")
    
def perform_fajr_prayer():
    # Fajr is the morning prayer, so it's one of the first things in my routine.
    print("Performing Fajr prayer...")

def eat_breakfast(food_item = "breakfast"): 
    # Prints whatever food is given. If nothing is given, it just says "breakfast".
    print(f"Eating {food_item}...")

def use_restroom():
    print("Using restroom and washing hands...")

def get_dressed(clothes = "default outfit"): 
    # Prints the clothes being worn. If nothing is given, it uses "default outfit".
    print(f"Getting dressed in {clothes}...")

def gather_belongings(stuff_to_take): 
    # Takes a list of items and prints them all on one line, separated by commas.
    print("Gathering belongings:", ", ".join(stuff_to_take))

def put_on_shoes_and_outerwear():
    print("Putting on shoes and outerwear...")

def leave_house():
    # The last step of the routine.
    print("Leaving the house. Have a good day at school!")

# This function calls every step above in order, from waking up to leaving the house.
def morning_routine():
    wake_up()
    
    brush_teeth()
    
    perform_fajr_prayer()
    
    # Stores what I'm eating and passes it into eat_breakfast().
    breakfast_choice = "cereal"
    eat_breakfast(breakfast_choice)
    
    use_restroom()
    
    get_dressed("school uniform")
    
    # A list of the items I need to bring to school.
    my_stuff = ["backpack", "books", "lunch", "keys", "phone"]
    gather_belongings(my_stuff)
    
    put_on_shoes_and_outerwear()
    
    leave_house()

# Runs the morning routine.
if __name__ == "__main__":
    morning_routine() 
