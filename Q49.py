
def superDigit(n, k):

    total = sum(int(digit) for digit in n) * k

    def find_digit(num):
        if num < 10:
            return num

        digit_sum = sum(int(digit) for digit in str(num))

        return find_digit(digit_sum)

    return find_digit(total)


# take input
n, k = input().split()

k = int(k)

# calculate super digit
answer = superDigit(n, k)

print(answer)
