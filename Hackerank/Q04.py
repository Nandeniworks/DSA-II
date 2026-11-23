#a very big sum 
def aVeryBigSum(ar):
    return sum(ar)

n = int(int(input("enter number of elements:")))
ar = list(map(int, input("enter the numbers: ").rstrip().split()))


result = aVeryBigSum(ar)
print(result)

    
