
n = int(input())

stack = []
max_stack = []

for i in range(n):
    query = input().split()

    if query[0] == '1':
        x = int(query[1])
        stack.append(x)

        if not max_stack or x >= max_stack[-1]:
            max_stack.append(x)
        else:
            max_stack.append(max_stack[-1])

    elif query[0] == '2':
        stack.pop()
        max_stack.pop()

    elif query[0] == '3':
        print(max_stack[-1])
