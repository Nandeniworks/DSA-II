class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLinkedList(head):
    current = head

    while current is not None:
        print(current.data)
        current = current.next


n = int(input())

head = None
tail = None

for i in range(n):
    value = int(input())
    new_node = Node(value)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

printLinkedList(head)