import random

# Each function below prints one step of studying for a test.

def clarify_what_im_studying():
    print("Figuring out what the test is about...")

def figure_out_timeline():
    print("Checking when the test is and how much time I have...")

def collect_study_stuff():
    print("Gathering notes, textbooks, and practice tests...")

def honest_self_check():
    print("Checking what I already know and what I still need to learn...")

def build_my_schedule():
    print("Making a study schedule...")

def actually_study():
    print("Studying: reading, taking notes, and doing practice problems...")

def practice_test_time():
    print("Taking a practice test...")

def find_my_weak_points():
    # Randomly picks True or False to act like the result of checking for weak spots.
    weak_spots_exist = random.choice([True, False])
    if weak_spots_exist:
        print("Found some topics I still need to work on.")
    else:
        print("No weak spots found. I understand all the topics.")
    # Sends the result back so study_for_test() knows whether to keep studying.
    return weak_spots_exist

def fix_weak_areas():
    print("Going back over the topics I struggled with...")

def do_review_sessions():
    print("Reviewing everything so I don't forget it...")

def practice_like_its_real():
    print("Taking a timed practice test like it's the real one...")

def last_minute_prep():
    print("Doing a final light review the day before the test...")

def get_ready_for_test_day():
    print("Packing my bag, setting alarms, and getting a good night's sleep...")

def test_day():
    print("Taking the test...")

def think_about_how_it_went():
    print("Thinking about what went well and what to do differently next time...")

# This function calls every step in order, from figuring out what to study to the test itself.
def study_for_test():
    clarify_what_im_studying()
    figure_out_timeline()
    collect_study_stuff()
    honest_self_check()
    build_my_schedule()
    
    # Counts how many times the study loop repeats.
    study_cycles = 0
    # This loop keeps repeating studying and practice tests until there are no weak spots left.
    while True:
        actually_study()
        practice_test_time()
        has_weak_spots = find_my_weak_points()
        
        if has_weak_spots:
            fix_weak_areas()
            study_cycles += 1
        else:
            # Adds 1 because the last cycle (the one with no weak spots) wasn't counted yet.
            total_cycles = study_cycles + 1
            # Uses "cycle" for 1 and "cycles" for more than 1.
            cycle_word = "cycle" if total_cycles == 1 else "cycles"
            print(f"It took {total_cycles} study {cycle_word}, but I'm ready for the test.")
            break
    
    do_review_sessions()
    practice_like_its_real()
    last_minute_prep()
    get_ready_for_test_day()
    test_day()
    think_about_how_it_went()

# Runs the whole study plan.
if __name__ == "__main__":
    print("Starting to study for the test...")
    study_for_test()
    print("Done! Good luck on the test!")
