

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def createList(values):
    head = None
    current = None

    for val in values:
        newNode = Node(val)

        if head is None:
            head = newNode
            current = newNode
        else:
            current.next = newNode
            current = newNode

    return head


def deleteDuplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next


head = createList([1, 1, 2, 3, 3])

result = deleteDuplicates(head)

printList(result)
