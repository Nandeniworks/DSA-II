def countingSort(arr):
    freq = [0] * 100

    for num in arr:
        freq[num] += 1

    result = []

    for i in range(100):
        for j in range(freq[i]):
            result.append(i)

    return result


n = int(input())
arr = list(map(int, input().split()))

result = countingSort(arr)
print(*result)