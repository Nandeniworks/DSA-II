
def wordPattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False

    map1 = {}
    map2 = {}

    for i in range(len(pattern)):
        ch = pattern[i]
        word = words[i]

        if ch in map1 and map1[ch] != word:
            return False

        if word in map2 and map2[word] != ch:
            return False

        map1[ch] = word
        map2[word] = ch

    return True


pattern = "abba"
s = "dog cat cat dog"

print(wordPattern(pattern, s))
