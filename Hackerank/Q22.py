
def funnyString(s):
    rev = s[::-1]

    for i in range(1, len(s)):
        original_diff = abs(ord(s[i]) - ord(s[i - 1]))
        reverse_diff = abs(ord(rev[i]) - ord(rev[i - 1]))

        if original_diff != reverse_diff:
            return "Not Funny"

    return "Funny"


q = int(input())

for _ in range(q):
    s = input()
    print(funnyString(s))
