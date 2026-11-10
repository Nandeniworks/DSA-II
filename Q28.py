def countingSort(arr):
    freq = [0] * 100

    for num in arr:
        freq[num] += 1

    return freq


n = int(input())
arr = list(map(int, input().split()))

result = countingSort(arr)
print(*result)