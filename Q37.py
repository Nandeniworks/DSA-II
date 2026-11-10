class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeAtPosition(head, data, position):
    new_node = Node(data)

    if position == 0:
        new_node.next = head
        return new_node

    current = head

    for i in range(position - 1):
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


def printLinkedList(head):
    current = head

    while current is not None:
        print(current.data, end=" ")
        current = current.next


n = int(input())

head = None
tail = None

for i in range(n):
    data = int(input())
    new_node = Node(data)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

data = int(input())
position = int(input())

head = insertNodeAtPosition(head, data, position)

printLinkedList(head)