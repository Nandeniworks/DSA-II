
def superReducedString(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        return "Empty String"

    return "".join(stack)


s = input()
result = superReducedString(s)
print(result)
