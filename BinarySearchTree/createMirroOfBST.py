class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def mirrorBinaryTree(root: TreeNode) -> TreeNode:
    if root is None:
        return None

    # Recursively mirror the left and right subtrees
    left = mirrorBinaryTree(root.left)
    right = mirrorBinaryTree(root.right)

    # Swap the left and right children
    root.left = right
    root.right = left
    return root
