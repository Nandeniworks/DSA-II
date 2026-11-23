
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def createList(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    return head


head = createList([1, 2, 3, 4, 5])

middle = middleNode(head)

print(middle.val)
