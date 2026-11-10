def findMedian(arr):
    arr.sort()
    mid = len(arr) // 2
    return arr[mid]


n = int(input())
arr = list(map(int, input().split()))

result = findMedian(arr)
print(result)