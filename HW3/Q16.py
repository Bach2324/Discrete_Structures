# CSCI 2824 -- Discrete Structures
# Author: Bach Nguyen
# Homework 3 - Problem #16

def ABCs(letters,numbers):
    vowels = ['A','E','I','O','U']
    for i in range(len(letters)):
        if (numbers[i] % 2 == 0):
            if(letters[i] not in vowels):
                return False
    return True

letters = ['A','B','C']
numbers = [ 1 , 2 , 3 ]
print(ABCs(letters, numbers))

letters = ['A','A','A','A']
numbers = [ 1 , 2 , 3 , 4 ]
print(ABCs(letters, numbers))

letters = ['Z','A','I','I', 'B' , 'U']
numbers = [ 1 , 20, 4 , 16, 123 , 100]
print(ABCs(letters, numbers))