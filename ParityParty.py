def ParityParty(d):
    a_list = []

    if (d % 2 == 0):
        a_list.append(0)
        a_list.append(int(d/2))
    else:
        a_list.append(1)
        a_list.append(int((d-1)/2))
    
    return a_list

print(ParityParty(10))
print(ParityParty(33))