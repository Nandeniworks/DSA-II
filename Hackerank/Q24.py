
def anagram(s):
    n = len(s)

    if n % 2 != 0:
        return -1

    half = n // 2
    s1 = s[:half]
    s2 = s[half:]

    count = 0

    for char in set(s1):
        diff = s1.count(char) - s2.count(char)

        if diff > 0:
            count += diff

    return count


q = int(input())

for _ in range(q):
    s = input()
    print(anagram(s))
