
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNode(head, position):

    # delete the first node
    if position == 0:
        return head.next

    current = head

    # reach the node before the position
    for i in range(position - 1):
        current = current.next

    # skip the node to delete
    current.next = current.next.next

    return head


# create linked list
head = Node(20)
head.next = Node(6)
head.next.next = Node(2)
head.next.next.next = Node(19)
head.next.next.next.next = Node(7)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(15)
head.next.next.next.next.next.next.next = Node(9)

position = 3

# delete the node
head = deleteNode(head, position)

# print the linked list
current = head

while current:
    print(current.data, end=" ")
    current = current.next
