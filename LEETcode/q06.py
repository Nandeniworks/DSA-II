
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


def mergeTwoLists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next


# test input
list1 = createList([1, 2, 4])
list2 = createList([1, 3, 4])

result = mergeTwoLists(list1, list2)

printList(result)
