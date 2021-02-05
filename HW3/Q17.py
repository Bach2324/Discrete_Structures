def check_proposition(aList):
    count = 0
    count2 = 0
    for i in range(len(aList)):
        if (aList[i] % 2 == 0):
            count = count + 1
            for j in range(len(aList)):
                if ((aList[j]*2) == aList[i]):
                    count2 = count2 + 1

    if (count != count2):
        return False                
    return True

print(check_proposition([-2,-1,0,1,2,3]))
print(check_proposition([-2,-1,0,1,3,4]))