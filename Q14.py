
def matchingStrings(stringList, queries):
    result = []

    for query in queries:
        count = stringList.count(query)
        result.append(count)

    return result


stringList_count = int(input())
stringList = []

for _ in range(stringList_count):
    stringList.append(input())

queries_count = int(input())
queries = []

for _ in range(queries_count):
    queries.append(input())

res = matchingStrings(stringList, queries)

for count in res:
    print(count)
