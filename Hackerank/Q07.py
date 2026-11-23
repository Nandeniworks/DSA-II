
def miniMaxSum(arr):
    total = sum(arr)
    minimum = total - max(arr)
    maximum = total - min(arr)

    print(minimum, maximum)


arr = list(map(int, input().split()))
miniMaxSum(arr)
