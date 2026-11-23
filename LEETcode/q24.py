
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root):
    if root is None:
        return 0

    if root.left is None:
        return 1 + minDepth(root.right)

    if root.right is None:
        return 1 + minDepth(root.left)

    left = minDepth(root.left)
    right = minDepth(root.right)

    return 1 + min(left, right)


# create the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(minDepth(root))
