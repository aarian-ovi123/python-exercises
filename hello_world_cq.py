import sys
import math
import string

answerstorage = [] # This is where our messages are going to be stored before it is printed out again. 
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    doubleMessage = input('') # This is where we type our messages.
    answerstorage.append(doubleMessage) # This is the function where it'll put our messages in a list above.

# This is the function where it'll go through every message in the list.    
for i in answerstorage:
    print(i)
