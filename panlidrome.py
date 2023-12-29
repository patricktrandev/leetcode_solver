def solvePalindrome(x):

    strx=str(x)
    if strx[::-1]==strx[::1]:
        return True
    return False


test=solvePalindrome(1)
print(test)

def solvePalindrome2(x):
    strx=str(x)
    for i in range(len(strx)):
        if strx[len(strx)-i-1]!=strx[i]:
            return False
    return True

test2=solvePalindrome2(12)
print(test2)