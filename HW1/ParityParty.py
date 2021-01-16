# CSCI 2824 -- Discrete Structures
# Author: Bach Nguyen
# Homework 1 - Problem #12

def ParityParty(d):
    a_list = []                     # Declaring our list to store the values

    if (d % 2 == 0):                # Evaluate if the argument is an even number
        a_list.append(0)            # Append 0 to the first index of the list
        a_list.append(int(d/2))     # Append the value divided by 2 (convert to int type) to the second index
    else:                           # Evaluate if argument is odd
        a_list.append(1)            # Append 1 to the first index of the list
        a_list.append(int((d-1)/2)) # Append value minus 1 and divide by 2 to the second index
    
    return a_list                   # Return the list

print(ParityParty(10))              # Test case 1
print(ParityParty(33))              # Test case 2