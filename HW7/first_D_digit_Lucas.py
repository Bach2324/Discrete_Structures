def first_D_digit_Lucas(D):
    l0 = 2
    l1 = 1
    while(len(str(l0)) < D):
        l2 = l0 + l1
        l0 = l1
        l1 = l2
    return l0
        
print(first_D_digit_Lucas(2))