
def introTutorial(V, arr):
    for i in range(len(arr)):
        if arr[i] == V:
            return i


V = int(input())
n = int(input())
arr = list(map(int, input().split()))

result = introTutorial(V, arr)
print(result)
