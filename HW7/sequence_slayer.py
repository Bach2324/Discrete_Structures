def sequence_slayer(N):     # Using recursive method to solve
    if (N == 0):            # base case given, if N is zero
        return 1            # return 1
    if (N == 1):            # base case 2 given, if N is one
        return 2            # return 2
    else:                   # otherwise, compute
        return ((N**2)*sequence_slayer(N-1))-sequence_slayer(N-2)

# a_n = N^2*(a_(n-1)) - a(n-2)
print(sequence_slayer(2))   # Test case 1
print(sequence_slayer(3))   # Test case 2
print(sequence_slayer(8))   # Test case 3