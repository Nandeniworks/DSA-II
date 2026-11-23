
def isBalanced(s):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:

        if ch in '([{':
            stack.append(ch)

        else:
            if not stack:
                return "NO"

            if stack[-1] != pairs[ch]:
                return "NO"

            stack.pop()

    if not stack:
        return "YES"

    return "NO"


# take input
n = int(input())

for i in range(n):
    s = input()
    print(isBalanced(s))
