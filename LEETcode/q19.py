
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isSameTree(p, q):
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return (isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right))


# first tree
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# second tree
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(isSameTree(p, q))
