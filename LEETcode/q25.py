
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    if root is None:
        return False

    targetSum -= root.val

    if root.left is None and root.right is None:
        return targetSum == 0

    return (hasPathSum(root.left, targetSum) or
            hasPathSum(root.right, targetSum))


# create the tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

targetSum = 22

print(hasPathSum(root, targetSum))
