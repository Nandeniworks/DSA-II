
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeElements(head, val):
    dummy = Node(0)
    dummy.next = head

    current = dummy

    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next


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


head = createList([1, 2, 6, 3, 4, 5, 6])

head = removeElements(head, 6)

printList(head)
