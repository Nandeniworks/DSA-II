
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postOrder(root):
    if root is None:
        return

    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=" ")


# create binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# perform postorder traversal
postOrder(root)
