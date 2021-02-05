# CSCI 2824 -- Discrete Structures
# Author: Bach Nguyen
# Homework 3 - Problem #15

def D(i,n):                         # Define our function
    aList = [4, 8, 15, 16, 23, 42]  # Define our list to check
    if (aList[i] % n == 0):         # If the value at index i is divisible by the given n
        return True                 # Function will return True
    return False                    # Return False otherwise

print(D(0,2))                       # Test case 1
print(D(1,3))                       # Test case 2
print(D(2,3))                       # Test case 3