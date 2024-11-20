# Definition for TreeNode
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(root):

    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def check_balanced(root):

    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if (
        (abs(lh - rh) <= 1)
        and check_balanced(root.left) is True
        and check_balanced(root.right) is True
    ):
        return True
    return False
