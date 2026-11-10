
def powerSum(X, N):

    def find_sum(num, total):
        power = num ** N

        if total == X:
            return 1

        if total > X or total + power > X:
            return 0

        include = find_sum(num + 1, total + power)
        exclude = find_sum(num + 1, total)

        return include + exclude


    return find_sum(1, 0)


# take input
X = int(input())
N = int(input())

# calculate answer
print(powerSum(X, N))
