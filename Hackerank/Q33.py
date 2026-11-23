def bigSorting(unsorted):
    return sorted(unsorted, key=int)


n = int(input())

unsorted = []

for i in range(n):
    num = input()
    unsorted.append(num)

result = bigSorting(unsorted)

for num in result:
    print(num)