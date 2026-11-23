
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderTraversal(root):
    result = []

    def inorder(node):
        if node is None:
            return

        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result


# create the binary tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorderTraversal(root))
