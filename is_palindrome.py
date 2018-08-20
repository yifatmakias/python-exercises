

def is_palindrome(x):
    index1 = 0
    index2 = len(x) - 1
    while index2 >= index1:
        if x[index1] != x[index2]:
            return False
        else:
            index1 += 1
            index2 -= 1
    return True


print(is_palindrome("not palindrom"))
print(is_palindrome("blaalb"))
