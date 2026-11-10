class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeAtTail(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next is not None:
        current = current.next

    current.next = new_node

    return head


def printLinkedList(head):
    current = head

    while current is not None:
        print(current.data)
        current = current.next


n = int(input())

head = None

for i in range(n):
    data = int(input())
    head = insertNodeAtTail(head, data)

printLinkedList(head)