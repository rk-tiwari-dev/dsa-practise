class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: TreeNode) -> int:
    max_diameter = 0  # To store the maximum diameter found

    def depth(node):
        nonlocal max_diameter
        if not node:
            return 0

        # Calculate the depth of left and right subtrees
        left_depth = depth(node.left)
        right_depth = depth(node.right)

        # Update the diameter if the path through the current node is longer
        max_diameter = max(max_diameter, left_depth + right_depth)

        # Return the height of the tree rooted at this node
        return max(left_depth, right_depth) + 1

    depth(root)
    return max_diameter
