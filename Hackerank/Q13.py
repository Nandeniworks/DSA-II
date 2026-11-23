
def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
        t, x, y = query
        idx = (x ^ lastAnswer) % n

        if t == 1:
            arr[idx].append(y)
        elif t == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers


n, q = map(int, input().split())

queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))

result = dynamicArray(n, queries)

for answer in result:
    print(answer)
