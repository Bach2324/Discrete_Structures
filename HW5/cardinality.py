# CSCI 2824 -- Discrete Structures
# Homework 5 -- Problem 11
# Bach Nguyen

def cardinality(A, B, U):
    # Since the cardinality of a power set is 2^n, where n is the number of elements
    # n will be equal to the U-(A-B)
    return 2**(len(set(U).difference(set(A).difference(B))))

A = {0, 2, 5, 10, 11, 12, 15, 16, 19, 23, 24, 30}
B = {1, 3, 4, 16}
U = set(list(range(0,31)))
print(cardinality(A, B, U))