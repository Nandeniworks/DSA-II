
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def compare_lists(head1, head2):

    while head1 and head2:

        if head1.data != head2.data:
            return 0

        head1 = head1.next
        head2 = head2.next

    if head1 is None and head2 is None:
        return 1

    return 0


# first linked list
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)

# second linked list
head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)

# compare both lists
print(compare_lists(head1, head2))
