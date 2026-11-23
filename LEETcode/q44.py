
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# create linked list: 3 -> 2 -> 0 -> -4
head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)

# create a cycle: -4 points back to 2
head.next.next.next.next = head.next

print(hasCycle(head))
