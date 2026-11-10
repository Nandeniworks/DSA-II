class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeAtHead(head, data):
    new_node = Node(data)

    new_node.next = head
    head = new_node

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
    head = insertNodeAtHead(head, data)

printLinkedList(head)