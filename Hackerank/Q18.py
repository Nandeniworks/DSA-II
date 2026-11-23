
def marsExploration(s):
    count = 0

    for i in range(len(s)):
        expected = "SOS"[i % 3]

        if s[i] != expected:
            count += 1

    return count


s = input()
print(marsExploration(s))
