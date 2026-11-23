
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)


# create tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# preorder traversal
preOrder(root)
