
def makingAnagrams(s1, s2):
    count = 0

    for char in set(s1 + s2):
        count += abs(s1.count(char) - s2.count(char))

    return count


s1 = input()
s2 = input()

result = makingAnagrams(s1, s2)
print(result)
