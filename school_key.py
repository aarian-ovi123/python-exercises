"""
Assignment:
Write a program that lets you know if you can have a key or not, based on your role at the school. Your program must use the logical or operator.

First ask for the user's role at the school. They can be a student, administrator, or a teacher. (And remember that capitalization is important! 'Student' is not the same as 'student'.)

(Note: You should also be able to handle a situation where the user enters a value other than administrator, teacher or student and tell them they must be one of the three choices!)
"""

school_role = input("What is your role at school? Are you a student, teacher, or an administrator? ").strip().lower() # Asks the user what their role is at school. .strip().lower() lets "Teacher" or " teacher " still work.

# Uses the "or" operator so both teachers and administrators can get a key.
if school_role == "student":
    print("Students cannot have a key.")
elif school_role == "teacher" or school_role == "administrator":
    print("Teachers and Administrators can have a key.")
else:
    print("You have to be one of three choices, which is either a student, teacher, or administrator!")
