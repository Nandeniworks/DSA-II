
def checkMagazine(magazine, note):
    words = {}

    for word in magazine:
        words[word] = words.get(word, 0) + 1

    for word in note:
        if words.get(word, 0) == 0:
            print("No")
            return

        words[word] -= 1

    print("Yes")


m, n = map(int, input().split())
magazine = input().split()
note = input().split()

checkMagazine(magazine, note)
