
def missingNumber(nums):
    n = len(nums)

    expectedSum = n * (n + 1) // 2
    actualSum = sum(nums)

    return expectedSum - actualSum


nums = [3, 0, 1]

print(missingNumber(nums))
