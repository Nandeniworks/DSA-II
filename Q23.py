
def pangrams(s):
    letters = set(s.lower())

    if len(letters.intersection(set("abcdefghijklmnopqrstuvwxyz"))) == 26:
        return "pangram"
    else:
        return "not pangram"


s = input()
print(pangrams(s))
