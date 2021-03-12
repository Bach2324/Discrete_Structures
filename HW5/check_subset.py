# CSCI 2824 -- Discrete Structures
# Homework 5 -- Problem 10
# Bach Nguyen

def check_subset(A,B):
    # Return True if one of the proposition is true
    # Return False if both are false (they're not subsets of each other)
    return set(B).issubset(set(A)) or set(A).issubset(set(B))  

A = {0, 2, 10, -5}
B = {-5, 10}
print(check_subset(A, B))

C = {0, 2, 4, 6}
D = {
print(check_subset(C, D))

E = {}
F = {1,2,3}
print(check_subset(E,F))