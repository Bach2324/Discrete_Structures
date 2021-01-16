# CSCI 2824 -- Discrete Structures
# Author: Bach Nguyen
# Homework 1 - Problem #13

def DecToBin(d):
    a_list = []                     # Declare list to store our binary values in
    for i in range(10):             # to traverse through the length of a binary value
        if (d == 0):                # When d reaches 0, we will break (stop) the loop
            if (i == 0):            # If the initial d value is zero, we add 0 to the list and stop the loop
                a_list.append(0)
            break                   # Stop the loop
        
        elif (d % 2 == 0):          # Evaluate if d is an even value
            d = d/2                 # Divide d in half
            a_list.insert(0, 0)     # Add/insert the corresponding binary value to the beginning of the list
        
        else:                       # Evaluate if d is odd
            d = (d-1)/2             # Subtract d by 1 and then divide by 2
            a_list.insert(0,1)      # Add/insert the corresponding binary value to the beginning of the list
    
    return a_list                   # Return the completed list

print(DecToBin(0))                  # Test case 1
print(DecToBin(10))                 # Test case 2
print(DecToBin(241))                # Test case 3
