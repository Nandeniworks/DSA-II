
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverseList(head):
    prev = None
    current = head

    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    return prev


def createList(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    return head


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = createList([1, 2, 3, 4, 5])

print("Original list:")
printList(head)

head = reverseList(head)

print("Reversed list:")
printList(head)
