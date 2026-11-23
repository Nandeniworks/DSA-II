
def isPalindrome(x):
    if x < 0:
        return False

    return str(x) == str(x)[::-1]


# test input
x = 121

result = isPalindrome(x)
print(result)
