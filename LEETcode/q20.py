
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isSymmetric(root):
    def isMirror(left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return (isMirror(left.left, right.right) and
                isMirror(left.right, right.left))

    return isMirror(root.left, root.right) if root else True


# create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))
