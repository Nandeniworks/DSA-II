
def diagonalDifference(arr):
    n = len(arr)
    left = 0
    right = 0

    for i in range(n):
        left += arr[i][i]
        right += arr[i][n - 1 - i]

    return abs(left - right)


n = int(input("Enter matrix size: "))

arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

result = diagonalDifference(arr)
print(result)
